
from fastembed import TextEmbedding
from fastembed import SparseTextEmbedding
from fastapi import HTTPException
dense_model = None
sparse_model = None


def get_dense_embedding(text):

    global dense_model
    try:

      if dense_model is None:

        dense_model = TextEmbedding(
            model_name="BAAI/bge-small-en-v1.5"
        )

      embedding = next(
        dense_model.embed([text])
      )
      return embedding.tolist()

    except Exception as e:
      print(f"Error occurred while generating dense embedding: {e}")
      raise HTTPException(status_code=500, detail="Failed to generate dense embedding") from e



def get_sparse_embedding(text):

    global sparse_model
    
    try:

     if sparse_model is None:

        sparse_model = SparseTextEmbedding(
            model_name="Qdrant/bm25"
        )

     embedding = next(
        sparse_model.embed([text])
     )

     return {
        "indices": embedding.indices.tolist(),
        "values": embedding.values.tolist()
    }
    except Exception as e:
      print(f"Error occurred while generating sparse embedding: {e}")
      raise HTTPException(status_code=500, detail="Failed to generate sparse embedding") from e