from qdrant_client.models import Distance, VectorParams, Datatype
from app.configs.qdrant import get_qdrant_client


COLLECTION_NAME = "rag_collection"

def create_collection():
    client = get_qdrant_client()
    check_collection = client.collection_exists(collection_name=COLLECTION_NAME)

    if not check_collection:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=1024,
                distance=Distance.COSINE,
                datatype=Datatype.UINT8,
            )
        )
        
        print(f"Collection '{COLLECTION_NAME}' created successfully.")
    else:
        print(f"Collection '{COLLECTION_NAME}' already exists.")  
        
    