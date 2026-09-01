import httpx

from app.core.config import settings
from app.core.exceptions import AIServiceException


class LLMClient:

    async def generate(
        self,
        prompt: str,
    ) -> str:

        url = (
            f"{settings.OLLAMA_URL}/api/generate"
        )

        payload = {
            "model": settings.OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
        }

        try:
            async with httpx.AsyncClient(
                timeout=120
            ) as client:

                response = await client.post(
                    url,
                    json=payload,
                )

                response.raise_for_status()

                data = response.json()

                return data.get(
                    "response",
                    "",
                )

        except Exception as exc:
            raise AIServiceException(
                f"LLM request failed: {exc}"
            )