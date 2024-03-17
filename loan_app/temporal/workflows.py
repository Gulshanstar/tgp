from datetime import timedelta
from temporalio import workflow
from temporalio.common import RetryPolicy

# Import our activity, passing it through the sandbox
with workflow.unsafe.imports_passed_through():
    import activities
    

@workflow.defn
class LoanProcess:
    @workflow.run
    async def run(self, name: str) -> str:
         
         steps1_res = await workflow.execute_activity(
            activities.steps1, name, schedule_to_close_timeout=timedelta(seconds=50)
        )
         steps2_res = await workflow.execute_activity(
            activities.steps2, name, schedule_to_close_timeout=timedelta(seconds=50)
        )
         steps3_res = await workflow.execute_activity(
            activities.steps3, name, schedule_to_close_timeout=timedelta(seconds=50)
        )
         steps4_res = await workflow.execute_activity(
           activities.steps4, name, schedule_to_close_timeout=timedelta(seconds=50)
        )
         steps5_res = await workflow.execute_activity(
            activities.steps5, name, schedule_to_close_timeout=timedelta(seconds=50)
        )
         steps6_res = await workflow.execute_activity(
            activities.steps6, name, schedule_to_close_timeout=timedelta(seconds=50)
        )
         
         return f"{steps2_res}"