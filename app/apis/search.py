from fastapi import APIRouter 
from app.retrieval.search import search
from app.retrieval.query_rewriter import rewrite_query
from app.retrieval.context_builder import build_context
from app.Generation.generator import generate_response
from app.evaluation.hallucination_checker import check_hallucination
from app.evaluation.evaluator import evaluate_model
router= APIRouter()

@router.get("/search/")
async def search_doc(query: str):
    
    rewriten_query =  await rewrite_query(query)
    results = await search(rewriten_query)
    context , citations = build_context(results)
    answer = await generate_response(rewriten_query, context)
    hallucination_check = await check_hallucination(context, answer)
    
    evaluation_data={
        "question": rewriten_query,
        "answer": answer,
        "contexts": [doc["text"] for doc in results],
        "ground_truth": ""
    }
    
    evaluation_result =  evaluate_model(evaluation_data)
    
    
    return {
        "original_query": query,
        "rewritten_query": rewriten_query,
        "answer": answer,
        "citations": citations,
        "hallucination_check": hallucination_check,
        "evaluation":str(evaluation_result)
    }    

    
    
    

    
