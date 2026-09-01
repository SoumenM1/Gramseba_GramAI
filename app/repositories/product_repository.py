from app.database.mongodb import get_collection


class ProductRepository:

    def __init__(self):
        self.collection = get_collection("products")

    async def get_by_id(self, product_id: str):
        return await self.collection.find_one({
            "_id": product_id
        })

    async def find_by_seller(self, seller_id: str):
        return await self.collection.find({
            "seller_id": seller_id
        }).to_list(length=100)