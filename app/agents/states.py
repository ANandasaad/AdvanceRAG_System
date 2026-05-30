from typing import TypedDict, Literal, List, Dict, Any
class GraphState(TypedDict):
    query: str
    query_status: Literal["VALID", "AMBIGUOUS", "NONSENSE", "UNSAFE", "OUT_OF_DOMAIN"]
    rewritten_query: str
    clarification_question: str
    retrieved_docs: List[Dict[str, Any]]
    generated_answer: str
    retry_count: int
    validation_pool:bool
    context: str
    citations: List[Dict[str, Any]]
    confidence:float
    

class QueryGate(TypedDict):
    query:str
    retrival_results:List[Dict[str,Any]]
    rerank_results:List[Dict[str,Any]]
    topK_results:List[Dict[str,Any]]