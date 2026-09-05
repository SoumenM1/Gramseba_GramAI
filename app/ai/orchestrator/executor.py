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

        # -------------------------
        # Seller search
        # -------------------------

        if plan["type"] == "seller_search":
            result = await self.sellers.handle(message)

            yield {
                "type": "sellers",
                "data": result,
            }

            return

        # -------------------------
        # Marketing
        # -------------------------

        if plan["type"] == "marketing":
            result = await self.marketing.handle(message)

            yield {
                "type": "marketing",
                "data": result,
            }

            return

        # -------------------------
        # Product search
        # -------------------------

        if plan["type"] == "product_search":
            result = await self.products.handle(message)

            # Send DB result immediately
            yield {
                "type": "products",
                "data": result,
            }

            # Then ask Ollama to explain
            prompt = f"""
                    User request:
                    {message}

                    Products found:
                    {result}

                    Explain the products naturally.
                    Do not invent product information.
                    """

            async for chunk in self.llm.generate(prompt):
                yield {
                    "type": "text",
                    "data": chunk,
                }

            return

        # -------------------------
        # General chat
        # -------------------------

        async for chunk in self.llm.generate(message):
            yield {
                "type": "text",
                "data": chunk,
            }

        return
