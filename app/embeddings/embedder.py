from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings

embedding_model= None


def get_embedding(text):
    
 global embedding_model

 if embedding_model is None:    
    embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
    encode_kwargs={"normalize_embeddings": True},
 )
    embedding_model = embeddings

    return embedding_model.embed_query(text)