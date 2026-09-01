from fastapi import APIRouter
from app.schemas.marketing import (
    MarketingRequest,
    MarketingResponse,
)
from app.services.marketing_service import MarketingService

router = APIRouter()
service = MarketingService()


@router.post("", response_model=MarketingResponse)
async def generate_marketing(request: MarketingRequest):
    result = await service.generate(request)

    return result