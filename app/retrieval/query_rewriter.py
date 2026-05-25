
from langchain_core.prompts import PromptTemplate
from app.llm.ollama_llm import chat_ollama

template = """
You are a retrieval query optimizer.

Rewrite the user query
to improve semantic retrieval.

Rules:
- Keep original intent
- Add missing technical context
- Make query specific
- Keep concise

User Query:
{query}

Rewritten Query:
"""

prompt= PromptTemplate(
    input_variables=["query"],
    template=template
)


async def rewrite_query(query:str) -> str:
    chain = prompt | chat_ollama
    
    result= chain.invoke({"query": query})
    
    return result.content.strip()