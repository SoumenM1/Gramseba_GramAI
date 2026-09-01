from app.database.mongodb import get_collection


class ConversationRepository:

    def __init__(self):
        self.collection = get_collection("conversations")

    async def save_message(
        self,
        conversation_id: str,
        user_id: str,
        role: str,
        content: str,
    ):
        await self.collection.update_one(
            {
                "_id": conversation_id,
                "user_id": user_id,
            },
            {
                "$push": {
                    "messages": {
                        "role": role,
                        "content": content,
                    }
                }
            },
            upsert=True,
        )

    async def get_conversation(
        self,
        conversation_id: str,
    ):
        return await self.collection.find_one({
            "_id": conversation_id
        })