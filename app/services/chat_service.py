
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

        # -------------------------
        # Create conversation ID
        # -------------------------

        if not conversation_id:
            conversation_id = str(uuid.uuid4())

        # Send conversation ID first
        yield {
            "type": "conversation",
            "conversation_id": conversation_id,
        }

        # -------------------------
        # Save user message
        # -------------------------

        await self.repository.save_message(
            conversation_id,
            user_id,
            "user",
            message,
        )

        # -------------------------
        # Stream AI response
        # -------------------------

        assistant_text = ""

        async for event in self.agent.run(
            user_id=user_id,
            message=message,
        ):

            # Collect only text for conversation history
            if event.get("type") == "text":
                assistant_text += event.get(
                    "data",
                    ""
                )

            # Forward event to controller
            yield event

        # -------------------------
        # Save complete AI response
        # -------------------------

        if assistant_text:

            await self.repository.save_message(
                conversation_id,
                user_id,
                "assistant",
                assistant_text,
            )

        # -------------------------
        # Stream finished
        # -------------------------

        yield {
            "type": "done",
        }

