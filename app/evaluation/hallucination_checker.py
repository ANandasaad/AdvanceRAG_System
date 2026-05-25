
from langchain_core.prompts import PromptTemplate
from fastapi import HTTPException
from app.llm.ollama_llm import chat_ollama
from app.prompts.rag_prompt import HALLUCINATION_PROMPT

prompt= PromptTemplate(
    input_variables=["context", "answer"],
    template=HALLUCINATION_PROMPT
)


async def check_hallucination(context, answer):
    try:
        chain = prompt | chat_ollama
        result= chain.invoke({
            "context": context,
            "answer": answer
        })
        
        return result.content.strip()
    except Exception as e:
        print(f"Error occurred while checking hallucination: {e}")
        raise HTTPException(status_code=500, detail="Failed to check hallucination") from e