from app.schemas.marketing import (
    MarketingRequest,
    MarketingResponse,
)
from app.ai.marketing.generator import MarketingGenerator


class MarketingService:

    def __init__(self):
        self.generator = MarketingGenerator()

    async def generate(
        self,
        request: MarketingRequest,
    ) -> MarketingResponse:

        return await self.generator.generate(
            request
        )