from app.llm.ollama_llm import chat_ollama
from langchain_core.prompts import PromptTemplate
from app.prompts.rag_prompt import RAG_PROMPTS

prompt = PromptTemplate(
    input_variables=["question", "context"],
    template=RAG_PROMPTS  
)

async def generate_response(question, context):
    
    chain = prompt | chat_ollama
    
    result = await chain.ainvoke({"question": question, "context": context})
    
    return result.content
    