import json
import traceback

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import StreamingResponse

from app.schemas.chat import ChatRequest
from app.services.chat_service import ChatService


router = APIRouter()
service = ChatService()

def sse(data: dict) -> str:
    """
    Convert data to Server-Sent Events format.
    """
    return f"data: {json.dumps(data, ensure_ascii=False)}\n\n"



@router.websocket("/ws")
async def chat_websocket(websocket: WebSocket):
    await websocket.accept()

    print("Client connected")

    try:
        while True:
            data = await websocket.receive_json()

            print("WS <-", data)

            user_id = data.get("user_id")
            message = data.get("message")
            conversation_id = data.get("conversation_id")

            if not user_id:
                await websocket.send_json({
                    "type": "error",
                    "data": "user_id is required",
                })
                continue

            if not message:
                await websocket.send_json({
                    "type": "error",
                    "data": "message is required",
                })
                continue

            async for event in service.chat(
                user_id=user_id,
                message=message,
                conversation_id=conversation_id,
            ):
                # print("WS ->", event)

                await websocket.send_json(event)

    except WebSocketDisconnect:
        print("Client disconnected")

    except Exception as exc:
        print("WebSocket error:")
        traceback.print_exc()

        try:
            await websocket.send_json({
                "type": "error",
                "data": str(exc),
            })
        except Exception:
            pass


@router.post("")
async def chat(request: ChatRequest):

    async def event_stream():

        try:
            async for chunk in service.chat(
                user_id=request.user_id,
                message=request.message,
                conversation_id=request.conversation_id,
            ):
                yield sse(chunk)

        except Exception as exc:
            yield sse(
                {
                    "type": "error",
                    "data": str(exc),
                }
            )

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
