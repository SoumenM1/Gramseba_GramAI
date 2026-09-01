from app.ai.marketing.generator import MarketingGenerator


class MarketingTools:

    def __init__(self):
        self.generator = MarketingGenerator()

    async def handle(self, message: str):

        return await self.generator.generate_from_text(
            message
        )