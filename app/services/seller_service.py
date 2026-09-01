from app.repositories.seller_repository import SellerRepository
from app.core.exceptions import SellerNotFoundException


class SellerService:

    def __init__(self):
        self.repository = SellerRepository()

    async def get_seller(self, seller_id: str):

        seller = await self.repository.get_by_id(
            seller_id
        )

        if not seller:
            raise SellerNotFoundException(
                "Seller not found"
            )

        return seller