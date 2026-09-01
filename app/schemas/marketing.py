from pydantic import BaseModel


class MarketingRequest(BaseModel):
    seller_id: str
    product_name: str
    language: str = "en"
    platform: str = "general"
    tone: str = "friendly"


class MarketingResponse(BaseModel):
    title: str
    description: str
    short_description: str
    hashtags: list[str]