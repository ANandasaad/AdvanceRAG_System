from langchain_core.prompts import PromptTemplate
from app.llm.ollama_llm import chat_ollama
from app.prompts.rag_prompt import GATE_PROMPT

prompt = PromptTemplate(
    input_variables=["query"],
    template=GATE_PROMPT
)


