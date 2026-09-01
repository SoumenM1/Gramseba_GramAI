from app.ai.memory.long_term import LongTermMemory


class MemoryService:

    def __init__(self):
        self.memory = LongTermMemory()

    async def get_memory(self, user_id: str):
        return await self.memory.get(user_id)