
from app.database.qdrant import get_qdrant_client


class VectorStore:

    def __init__(self):
        self.client = get_qdrant_client()

    async def search(
        self,
        collection_name: str,
        vector: list[float],
        limit: int = 5,
    ):
        return self.client.search(
            collection_name=collection_name,
            query_vector=vector,
            limit=limit,
        )