from fastapi import Header, HTTPException


async def authenticate(
    authorization: str | None = Header(default=None),
):

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Authorization required",
        )

    return authorization