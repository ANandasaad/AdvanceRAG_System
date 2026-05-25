from sentence_transformers import CrossEncoder

from fastapi import HTTPException
model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank(query, retrieved_docs):
    
    try:
        pairs = [
            (str(query), str(doc.payload.get('text', '')))
            for doc in retrieved_docs
        ]

        scores = model.predict(pairs)

        scored_docs = []
        for doc, score in zip(retrieved_docs, scores):
            scored_docs.append({
                "text": doc.payload['text'],
                "qdrant_score": float(doc.score),
                "re_rankscore": float(score),
                "source": doc.payload.get("source", "unknown"),
                "page": doc.payload.get("page", 0)
            })

        reranked_docs = sorted(scored_docs, key=lambda x: x['re_rankscore'], reverse=True)
        return reranked_docs
    
    except Exception as e:
        print(f"Error occurred during re-ranking: {e}")
        raise HTTPException(status_code=500, detail="Failed to re-rank documents") from e
    