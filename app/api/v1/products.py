from fastapi import APIRouter
from app.services.product_service import ProductService

router = APIRouter()
service = ProductService()


@router.get("/{product_id}")
async def get_product(product_id: str):
    return await service.get_product(product_id)