from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter()
service = ChatService()


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response = await service.chat(
        user_id=request.user_id,
        message=request.message,
        conversation_id=request.conversation_id,
    )

    return ChatResponse(
        response=response,
        conversation_id=request.conversation_id,
    )