import re
import uuid

from app.ai.orchestrator.agent import GramAIAgent
from app.repositories.conversation_repository import ConversationRepository


class ChatService:

    GREETING_RESPONSE = "I am Gram AI. How can I help you today?"

    GREETING_PATTERN = re.compile(
        r"^(hii|hello|hey|good morning|good afternoon|good evening)"
        r"(\s+gram(\s+ai)?)?[\s!,.?]*$",
        re.IGNORECASE,
    )

    def __init__(self):
        self.agent = GramAIAgent()
        self.repository = ConversationRepository()

    def is_greeting(self, message: str) -> bool:
        return bool(self.GREETING_PATTERN.match(message.strip()))

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

       
        if self.is_greeting(message):
            response = self.GREETING_RESPONSE
        else:
       
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

