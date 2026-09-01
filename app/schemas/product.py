from pydantic import BaseModel


class Product(BaseModel):
    id: str
    seller_id: str
    name: str
    description: str | None = None
    price: float | None = None
    category: str | None = None