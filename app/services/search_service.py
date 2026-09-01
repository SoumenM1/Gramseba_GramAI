from app.ai.tools.search_tools import SearchTools


class SearchService:

    def __init__(self):
        self.tools = SearchTools()

    async def search(self, query: str):
        return await self.tools.search(query)