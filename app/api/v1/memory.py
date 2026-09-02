from fastapi import APIRouter

from app.services.memory_service import MemoryService

router = APIRouter()
service = MemoryService()


@router.get("/{user_id}")
async def get_memory(user_id: str):
    return await service.get_memory(user_id)