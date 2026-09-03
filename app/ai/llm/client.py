import httpx
import logging
from app.ai.llm.prompts import GENERAL_CHAT_PROMPT
from app.core.config import settings
from app.core.exceptions import AIServiceException


class LLMClient:

    async def generate(
        self,
        prompt: str,
    ) -> str:

        url = (
            f"{settings.OLLAMA_URL}/api/chat"
        )

        payload = {
            "model": settings.OLLAMA_MODEL,
            "messages": [{"role": "system", "content": GENERAL_CHAT_PROMPT}, {"role": "user", "content": prompt}],
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
            logging.info(f"LLM response: {data}")
            
            return data.get("message", {}).get("content", "")
        
        except Exception as exc:
            raise AIServiceException(
                f"LLM request failed: {exc}"
            )