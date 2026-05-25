from datasets import Dataset, Features, Sequence, Value
from ragas import evaluate
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
)
from fastapi import HTTPException
from langchain_huggingface import HuggingFaceEmbeddings
from app.llm.ollama_llm import chat_ollama

ragas_ollama_llm = LangchainLLMWrapper(chat_ollama)
ragas_embeddings = LangchainEmbeddingsWrapper(
    HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
)

EVALUATION_FEATURES = Features(
    {
        "question": Value("string"),
        "answer": Value("string"),
        "contexts": Sequence(Value("string")),
        "ground_truth": Value("string"),
    }
)


def evaluate_model(data):
    try:
        if isinstance(data, dict):
            data = [data]
        elif not isinstance(data, list):
            raise ValueError("Evaluation data must be a dict or a list of dicts")

        dataset = Dataset.from_list(data, features=EVALUATION_FEATURES)
        print("Dataset for evaluation:", dataset)
        result = evaluate(
            dataset=dataset,
            metrics=[
                faithfulness,
                answer_relevancy,
                context_precision,
                context_recall,
            ],
            llm=ragas_ollama_llm,
            embeddings=ragas_embeddings,
        )
        return result
    except Exception as e:
        print(f"Error occurred during evaluation: {e}")
        raise HTTPException(status_code=500, detail="Failed to evaluate model") from e
    