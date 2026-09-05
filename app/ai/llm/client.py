import json
import logging
import httpx

from app.ai.llm.prompts import SYSTEM_PROMPT_ONE,SYSTEM_PROMPT_TWO
from app.core.config import settings
from app.core.exceptions import AIServiceException


logger = logging.getLogger(__name__)


class LLMClient:
    async def generate(self, prompt: str):

        url = f"{settings.OLLAMA_URL}/api/chat"

        payload = {
            "model": settings.OLLAMA_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT_TWO,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            "stream": True,
        }

        try:
            async with httpx.AsyncClient(timeout=None) as client:
                async with client.stream(
                    "POST",
                    url,
                    json=payload,
                ) as response:
                    response.raise_for_status()

                    async for line in response.aiter_lines():
                        if not line:
                            continue

                        try:
                            data = json.loads(line)

                            content = data.get("message", {}).get("content", "")

                            if content:
                                yield content

                            if data.get("done"):
                                break

                        except json.JSONDecodeError:
                            logger.warning(
                                "Invalid Ollama response: %s",
                                line,
                            )

        except httpx.HTTPError as exc:
            logger.exception("Ollama HTTP request failed")

            raise AIServiceException(f"LLM request failed: {exc}") from exc

        except Exception as exc:
            logger.exception("Ollama streaming failed")

            raise AIServiceException(f"LLM streaming failed: {exc}") from exc
