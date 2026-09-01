from app.repositories.product_repository import ProductRepository


class ProductTools:

    def __init__(self):
        self.repository = ProductRepository()

    async def find_by_seller(self, seller_id: str):

        return await self.repository.find_by_seller(
            seller_id
        )