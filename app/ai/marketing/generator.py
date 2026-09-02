import json
import re

from app.ai.llm.client import LLMClient
from app.schemas.marketing import (
    MarketingRequest,
    MarketingResponse,
)


class MarketingGenerator:
    def __init__(self):
        self.llm = LLMClient()

    async def generate(
        self,
        request: MarketingRequest,
    ):

        prompt = f"""
Create marketing content.

Product:
{request.product_name}

Language:
{request.language}

Platform:
{request.platform}

Tone:
{request.tone}

Return JSON:
{{
    "title": "...",
    "description": "...",
    "short_description": "...",
    "hashtags": ["...", "..."]
}}
"""

        response = await self.llm.generate(prompt)
        try:
            cleaned_response = response.strip()

            if cleaned_response.startswith("```"):
                cleaned_response = re.sub(
                    r"^```(?:json)?\s*|\s*```$",
                    "",
                    cleaned_response,
                    flags=re.IGNORECASE,
                ).strip()

            data = json.loads(cleaned_response)

        except json.JSONDecodeError:
            data = {
                "title": response,
                "description": response,
                "short_description": response[:150],
                "hashtags": [],
            }

        return MarketingResponse(**data)

    async def generate_from_text(
        self,
        message: str,
    ):

        return await self.llm.generate(
            f"""
Create marketing content from:

{message}
"""
        )
