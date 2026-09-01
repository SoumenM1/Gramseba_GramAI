from pydantic import BaseModel


class LLMResponse(BaseModel):
    response: str
    model: str | None = None
    tokens_used: int | None = None