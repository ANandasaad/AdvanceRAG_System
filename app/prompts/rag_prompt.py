

RAG_PROMPTS = """
You are an AI assistant.

Answer ONLY from the provided context.

Rules:
- Do NOT hallucinate
- If answer not found, say:
  "I could not find this information."
- Cite sources using citation numbers.

Context:
{context}

Question:
{question}

Answer:
"""
