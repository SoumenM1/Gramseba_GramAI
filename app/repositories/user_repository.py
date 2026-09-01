from app.database.mongodb import get_collection


class UserRepository:

    def __init__(self):
        self.collection = get_collection("users")

    async def get_by_id(self, user_id: str):
        return await self.collection.find_one({
            "_id": user_id
        })