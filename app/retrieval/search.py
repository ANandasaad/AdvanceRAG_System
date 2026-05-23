from app.embeddings.embedder import get_dense_embedding, get_sparse_embedding
from app.configs.qdrant import get_qdrant_client
from qdrant_client.models import Fusion, FusionQuery
COLLECTION_NAME = "rag_collection"

async def search(query: str):
    # Placeholder for search logic

    client = get_qdrant_client()
    dense_vector = get_dense_embedding(query)
    sparse_vector = get_sparse_embedding(query)

    search_result = client.query_points(
        collection_name=COLLECTION_NAME,
        prefetch=[
             {
                "query":    dense_vector,
                "using": "dense",
                "limit": 10
            },

            {
                "query":    sparse_vector,
                "using": "sparse",
                "limit": 10
            }
        ],
        
        query=FusionQuery(
            fusion=Fusion.RRF
        ),
        limit= 5
        
        
    )

    return search_result