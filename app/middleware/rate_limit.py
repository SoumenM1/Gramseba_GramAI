from fastapi import Request
from app.core.config import settings


async def rate_limit(request: Request):
    # Production implementation should use Redis.
    return True