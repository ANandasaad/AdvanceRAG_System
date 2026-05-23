from qdrant_client.models import Distance, VectorParams, Datatype, SparseVectorParams
from app.configs.qdrant import get_qdrant_client


COLLECTION_NAME = "rag_collection"

def create_collection():
    client = get_qdrant_client()
    check_collection = client.collection_exists(collection_name=COLLECTION_NAME)

    if not check_collection:
        client.create_collection(
            collection_name=COLLECTION_NAME,
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
        
        print(f"Collection '{COLLECTION_NAME}' created successfully.")
    else:
        print(f"Collection '{COLLECTION_NAME}' already exists.")  
        
    