from app.ai.llm.client import LLMClient
from app.ai.tools.seller_tools import SellerTools
from app.ai.tools.product_tools import ProductTools
from app.ai.tools.marketing_tools import MarketingTools


class Executor:

    def __init__(self):
        self.llm = LLMClient()
        self.sellers = SellerTools()
        self.products = ProductTools()
        self.marketing = MarketingTools()

    async def execute(
        self,
        plan: dict,
        user_id: str,
        message: str,
        
    ):

        if plan["type"] == "seller_search":
            return await self.sellers.handle(message)

        if plan["type"] == "marketing":
            return await self.marketing.handle(message)

        return await self.llm.generate(
            message
        )