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

from app.ingestions.buildmeta_data import build_meta_data

from app.retrieval.collection_maper import source_type

def index_chunks(chunks, document):

    client = get_qdrant_client()

    collection_name = source_type(document.source_type)

    texts = []

    for chunk in chunks:
        text = (
            chunk.page_content
            if hasattr(chunk, "page_content")
            else str(chunk)
        )
        texts.append(text)

    dense = get_dense_embedding(texts)
    sparse = get_sparse_embedding(texts)


    points = []

    for i, chunk in enumerate(chunks):

        text = texts[i]


        
        
        metadata= build_meta_data(document, chunk_index=i)
        
        metadata["text"]= text
        metadata["source_type"]= chunk.metadata.get("source_type", "unknown")
        metadata["title"]= chunk.metadata.get("title")

        point = PointStruct(

            id=str(uuid.uuid4()),
            vector={

                # dense vector
                "dense": dense[i],

                # sparse vector
                "sparse": SparseVector(
                    indices=sparse[i]["indices"],
                    values=sparse[i]["values"]
                )
            },
            
              
            payload=metadata
        )

        points.append(point)

    client.upsert(
        collection_name=collection_name,
        points=points
    )

    print(
        f"Indexed {len(points)} chunks into collection '{collection_name}'."
    )