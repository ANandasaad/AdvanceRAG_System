from app.embeddings.embedder import get_embedding
from app.configs.qdrant import get_qdrant_client

COLLECTION_NAME = "rag_collection"

async def search(query: str):
    # Placeholder for search logic

    client = get_qdrant_client()
    vector = get_embedding(query)

    search_result = client.query_points(
        collection_name=COLLECTION_NAME,
        query=vector,
        limit=5,
    )

    return search_result