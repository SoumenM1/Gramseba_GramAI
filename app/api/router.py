from fastapi import APIRouter

from app.core.config import settings
from app.api.v1.chat import router as chat_router
from app.api.v1.marketing import router as marketing_router
from app.api.v1.sellers import router as seller_router
from app.api.v1.products import router as product_router
from app.api.v1.search import router as search_router
from app.api.v1.memory import router as memory_router
from app.api.v1.health import router as health_router


api_router = APIRouter(prefix=settings.API_PREFIX)

api_router.include_router(chat_router, prefix="/chat", tags=["Chat"])
api_router.include_router(marketing_router, prefix="/marketing", tags=["Marketing"])
api_router.include_router(seller_router, prefix="/sellers", tags=["Sellers"])
api_router.include_router(product_router, prefix="/products", tags=["Products"])
api_router.include_router(search_router, prefix="/search", tags=["Search"])
api_router.include_router(memory_router, prefix="/memory", tags=["Memory"])
api_router.include_router(health_router, prefix="/health", tags=["Health"])