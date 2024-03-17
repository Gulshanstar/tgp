import asyncio
import concurrent.futures
from temporalio.client import Client
from temporalio.worker import Worker
# from prometheus_client import CollectorRegistry, Gauge, start_http_server
import prometheus_client
import threading
import time

# Import the activity and workflow from our other files
import activities
import workflows

def register_temporal_metrics():
    # Define your temporal metrics here, for example:
    global temporal_metric
    temporal_metric = prometheus_client.Gauge('temporal_metric', 'Description of temporal metric')

# Define a function to register JVM thread metrics
def register_jvm_thread_metrics():
    # You can implement JVM thread metrics here if needed
    pass

# Function to simulate your `MeterRegistry` setup
def meter_registry():
    # Create a CollectorRegistry
    registry = prometheus_client.CollectorRegistry()

    # Register temporal metrics
    register_temporal_metrics()

    # Register JVM thread metrics
    register_jvm_thread_metrics()

    return registry

# Function to start HTTP server
def start_server():
    prometheus_client.start_http_server(8000)
    # while True:
    #     time.sleep(1)

async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Run the worker
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as activity_executor:
        worker = Worker(
          client,
          task_queue="my-task-queue",
          workflows=[workflows.LoanProcess],
          activities=[activities.steps1, activities.steps2,activities.steps3,activities.steps4,activities.steps5,activities.steps6],
          activity_executor=activity_executor,
        )
        
        #  Start the Temporal worker
        # worker_thread = threading.Thread(target=worker.run)
        # worker_thread.daemon = True  # Daemonize thread so it shuts down when the main program exits
        # worker_thread.start()

        # Create your meter registry
        registry = meter_registry()
        
        # Start the HTTP server for Prometheus metrics
        start_server()
        await worker.run()

if __name__ == "__main__":
    asyncio.run(main())