from app.repositories.product_repository import ProductRepository
from app.core.exceptions import ProductNotFoundException


class ProductService:

    def __init__(self):
        self.repository = ProductRepository()

    async def get_product(self, product_id: str):

        product = await self.repository.get_by_id(
            product_id
        )

        if not product:
            raise ProductNotFoundException(
                "Product not found"
            )

        return product