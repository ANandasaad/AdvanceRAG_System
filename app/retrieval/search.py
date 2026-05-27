from app.embeddings.embedder import get_dense_embedding, get_sparse_embedding
from app.configs.qdrant import get_qdrant_client
from qdrant_client.models import Fusion, FusionQuery
from app.reranking.reranker import rerank
COLLECTION_NAME = "jira_chunks"

async def search(query: str):
    client = get_qdrant_client()

    dense_vectors = get_dense_embedding([query])
    sparse_vectors = get_sparse_embedding([query])

    dense_vector = dense_vectors[0]
    sparse_vector = sparse_vectors[0]

    search_result = client.query_points(
        collection_name=COLLECTION_NAME,
        prefetch=[
            {
                "query": dense_vector,
                "using": "dense",
                "limit": 20,
            },
            {
                "query": sparse_vector,
                "using": "sparse",
                "limit": 20,
            },
        ],
        
        query=FusionQuery(
            fusion=Fusion.RRF
        ),
        limit= 10
        
        
    )
    
    
    
    
    reranked_results = rerank(query, search_result.points)
    return reranked_results