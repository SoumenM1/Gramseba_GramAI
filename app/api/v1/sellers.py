from fastapi import APIRouter

from app.services.seller_service import SellerService

router = APIRouter()
service = SellerService()


@router.get("/{seller_id}")
async def get_seller(seller_id: str):
    return await service.get_seller(seller_id)