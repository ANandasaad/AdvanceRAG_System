
from fastembed import TextEmbedding
from fastembed import SparseTextEmbedding
from fastapi import HTTPException
dense_model = None
sparse_model = None


def get_dense_embedding(texts):

    global dense_model
    try:

      if dense_model is None:

        dense_model = TextEmbedding(
            model_name="BAAI/bge-small-en-v1.5"
        )

      embeddings = list(
        dense_model.embed(texts)
      )
      return [
            embedding.tolist()
            for embedding in embeddings
        ]

    except Exception as e:
      print(f"Error occurred while generating dense embedding: {e}")
      raise HTTPException(status_code=500, detail="Failed to generate dense embedding") from e



def get_sparse_embedding(texts):

    global sparse_model
    
    try:

     if sparse_model is None:

        sparse_model = SparseTextEmbedding(
            model_name="Qdrant/bm25"
        )

     embeddings = list(
        sparse_model.embed(texts)
     )

     sparse_vectors = []

     for embedding in embeddings:

            sparse_vectors.append({

                "indices":
                    embedding.indices.tolist(),

                "values":
                    embedding.values.tolist()
            })

     return sparse_vectors
    
    except Exception as e:
      print(f"Error occurred while generating sparse embedding: {e}")
      raise HTTPException(status_code=500, detail="Failed to generate sparse embedding") from e