from app.repositories.seller_repository import SellerRepository


class SearchTools:

    def __init__(self):
        self.seller_repository = SellerRepository()

    async def search(self, query: str):

        sellers = await self.seller_repository.find_by_name(
            query
        )

        return {
            "query": query,
            "results": sellers,
        }