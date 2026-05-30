from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)

def chunking(document):
    print("-----------")
    
    print(document["source_type"], "source")
    docs=[
        Document(
            page_content=document["content"],
            metadata={
                "id": document["id"],
                "doc_id": document["doc_id"],
                "source_type": document["source_type"],
                "title": document['title']
            }
        )
    ]
    return text_splitter.split_documents(docs)
