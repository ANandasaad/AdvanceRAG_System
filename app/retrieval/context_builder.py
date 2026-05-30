

def build_context(documents):
    
    context=""
    citations=[]
    
    for i, doc in enumerate(documents):        
        citation_id = f"{i+1}"
        text= doc["text"]
        doc_id= doc["doc_id"]
        source_type=doc["source"]
        
        
        context += (f"{citation_id}\n"
                    f"{doc['text']}\n\n"
                    )
        citations.append({
            "id": citation_id,
            "text": text,
            "doc_id": doc_id,
            "source":source_type
            
        })
        
    return context, citations
        
        
        
        
        