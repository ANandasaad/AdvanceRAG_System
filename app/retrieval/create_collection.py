from qdrant_client.models import Distance, VectorParams, Datatype, SparseVectorParams
from app.configs.qdrant import get_qdrant_client



collections = [
    "slack_chunks",
    "gmail_chunks",
    "github_chunks",
    "jira_chunks",
    "confluence_chunks",
    "fireflies_chunks"
]
def create_collection():
    client = get_qdrant_client()

    for collection in collections:
        check_collection = client.collection_exists(collection_name=collection)

        if not check_collection:
            client.create_collection(
                collection_name=collection,
                vectors_config={
                    "dense": VectorParams(
                        size=384,
                        distance=Distance.COSINE,
                        datatype=Datatype.UINT8,
                    )
                },
                sparse_vectors_config={
                    "sparse": SparseVectorParams()
                }
            )
            print(f"Collection '{collection}' created successfully.")
        else:
            print(f"Collection '{collection}' already exists.")
        