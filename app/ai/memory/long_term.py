from app.database.mongodb import get_collection


class LongTermMemory:

    def __init__(self):
        self.collection = get_collection(
            "user_memory"
        )

    async def save(
        self,
        user_id: str,
        memory: dict,
    ):

        await self.collection.update_one(
            {"user_id": user_id},
            {"$set": memory},
            upsert=True,
        )

    async def get(self, user_id: str):

        return await self.collection.find_one({
            "user_id": user_id
        })