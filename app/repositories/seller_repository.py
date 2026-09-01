from app.database.mongodb import get_collection


class SellerRepository:

    def __init__(self):
        self.collection = get_collection("sellers")

    async def get_by_id(self, seller_id: str):
        return await self.collection.find_one({
            "_id": seller_id
        })

    async def find_by_name(self, name: str):
        return await self.collection.find({
            "name": {
                "$regex": name,
                "$options": "i",
            }
        }).to_list(length=20)