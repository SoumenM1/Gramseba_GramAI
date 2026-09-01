from app.repositories.seller_repository import SellerRepository


class SellerTools:

    def __init__(self):
        self.repository = SellerRepository()

    async def handle(self, query: str):

        sellers = await self.repository.find_by_name(
            query
        )

        if not sellers:
            return (
                "I couldn't find a matching seller "
                "in the database."
            )

        return str(sellers)