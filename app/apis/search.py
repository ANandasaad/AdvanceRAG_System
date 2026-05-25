from fastapi import APIRouter 
from app.retrieval.search import search
from app.retrieval.query_rewriter import rewrite_query
from app.retrieval.context_builder import build_context
from app.Generation.generator import generate_response

router= APIRouter()

@router.get("/search/")
async def search_doc(query: str):
    rewriten_query = rewrite_query(query)
    results = await search(rewriten_query)
    context , citations = build_context(results)
    answer = await generate_response(rewriten_query, context)
    return {
        "original_query": query,
        "rewritten_query": rewriten_query,
        "answer": answer,
        "citations": citations
    }    

    
    
    

    
