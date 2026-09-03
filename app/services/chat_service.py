
import uuid

from app.ai.orchestrator.agent import GramAIAgent
from app.repositories.conversation_repository import ConversationRepository


class ChatService:


    def __init__(self):
        self.agent = GramAIAgent()
        self.repository = ConversationRepository()

    async def chat(
        self,
        user_id: str,
        message: str,
        conversation_id: str | None = None,
    ):

        if not conversation_id:
            conversation_id = str(uuid.uuid4())

   
        await self.repository.save_message(
            conversation_id,
            user_id,
            "user",
            message,
        )

        response = await self.agent.run(
                user_id=user_id,
                message=message,
            )

       
        await self.repository.save_message(
            conversation_id,
            user_id,
            "assistant",
            response,
        )

        return response

