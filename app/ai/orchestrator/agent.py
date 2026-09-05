
from app.ai.orchestrator.planner import Planner
from app.ai.orchestrator.executor import Executor
from app.ai.guardrails.input_guard import validate_input


class GramAIAgent:

    def __init__(self):
        self.planner = Planner()
        self.executor = Executor()

    async def run(
        self,
        user_id: str,
        message: str,
    ):

        validate_input(message)

        # Planner is still normal request/response
        plan = await self.planner.create_plan(message)

        # Executor is STREAMING
        async for event in self.executor.execute(
            plan=plan,
            user_id=user_id,
            message=message,
        ):
            yield event
