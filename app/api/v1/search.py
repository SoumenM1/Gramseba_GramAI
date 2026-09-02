from fastapi import APIRouter

from app.services.search_service import SearchService

router = APIRouter()
service = SearchService()


@router.get("")
async def search(q: str):
    return await service.search(q)