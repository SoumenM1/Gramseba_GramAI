import asyncio

from app.ai.llm.client import LLMClient


async def main():

    llm = LLMClient()

    response = await llm.generate(
        "Say hello as GramAI."
    )

    print(response)


if __name__ == "__main__":
    asyncio.run(main())