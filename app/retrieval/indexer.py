import uuid
from qdrant_client.models import PointStruct
from app.configs.qdrant import get_qdrant_client
from app.embeddings.embedder import get_embedding
COLLECTION_NAME = "rag_collection"



def index_chunks(chunks):
    client= get_qdrant_client()
    points = []
    
    for chunk in chunks:
        
        point= PointStruct(
            id= str(uuid.uuid4()),
            vector= get_embedding(chunk.page_content),
            payload={
                "text": chunk.page_content,
                "source": chunk.metadata.get("source", "unknown"),
                "page": chunk.metadata.get("page", 0)
            }
        )
        points.append(point)
        
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )
    print(f"Indexed {len(points)} chunks into collection '{COLLECTION_NAME}'.")