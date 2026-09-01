from pydantic import BaseModel


class Seller(BaseModel):
    id: str
    name: str
    business_name: str | None = None
    category: str | None = None
    location: dict | None = None