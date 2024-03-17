from temporalio import activity
from datetime import timedelta
import prometheus_client

# # Define Prometheus gauges for success and failure counts of each activity
activity_success_gauges = {}
activity_success_gauges2 = {}
activity_failure_gauges = {}
activity_failure_gauges2 = {}



@activity.defn
def steps1(name: str) -> str:
    activity_success_gauges.setdefault('steps1', prometheus_client.Gauge('activity_success_count_steps1', 'Number of successful executions for steps1'))
    activity_failure_gauges.setdefault('steps1', prometheus_client.Gauge('activity_failure_count_steps1', 'Number of failed executions for steps1'))
    
    try:
        # Execute steps1 logic
        
        activity_success_gauges['steps1'].inc()
        return f"Hello, 111!"
    except Exception as e:
        activity_failure_gauges['steps1'].inc()
        raise e

@activity.defn
def steps2(name: str) -> str:
    activity_success_gauges2.setdefault('steps2', prometheus_client.Gauge('activity_success_count_steps2', 'Number of successful executions for steps2'))
    activity_failure_gauges2.setdefault('steps2', prometheus_client.Gauge('activity_failure_count_steps2', 'Number of failed executions for steps2'))
    
    try:
        # Execute steps1 logic
        
        activity_success_gauges2['steps2'].inc()
        return f"Hello, 222222!"
    except Exception as e:
        activity_failure_gauges2['steps2'].inc()
        raise e

@activity.defn
def steps3(name: str) -> str:
    try:
        # Execute steps1 logic
        
        number = 7/0
        print(number)
        return f"Hello, 222222!"
    except Exception as e:
        
        raise e


@activity.defn
def steps4(name: str) -> str:
    return f"Hello, 4!"

@activity.defn
def steps5(name: str) -> str:
    return f"Hello, 5!"

@activity.defn
def steps6(name: str) -> str:
    return f"Hello, 6!"

