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

        plan = await self.planner.create_plan(
            message
        )

        result = await self.executor.execute(
            plan= {"type": "general_chat", "requires_database": False},
            user_id=user_id,
            message=message,
        )

        return result