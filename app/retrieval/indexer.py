import uuid

from qdrant_client.models import (
    PointStruct,
    SparseVector
)

from app.configs.qdrant import get_qdrant_client

from app.embeddings.embedder import (
    get_dense_embedding,
    get_sparse_embedding
)

COLLECTION_NAME = "rag_collection"


def index_chunks(chunks):

    client = get_qdrant_client()

    points = []

    for chunk in chunks:

        text = (
            chunk.page_content
            if hasattr(chunk, "page_content")
            else str(chunk)
        )

        dense = get_dense_embedding(text)

        sparse = get_sparse_embedding(text)

        point = PointStruct(

            id=str(uuid.uuid4()),

            vector={

                # dense vector
                "dense": dense,

                # sparse vector
                "sparse": SparseVector(
                    indices=sparse["indices"],
                    values=sparse["values"]
                )
            },

            payload={
                "text": text
            }
        )

        points.append(point)

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    print(
        f"Indexed {len(points)} chunks into collection '{COLLECTION_NAME}'."
    )