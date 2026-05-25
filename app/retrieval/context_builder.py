

def build_context(documents):
    
    context=""
    citations=[]
    
    for i, doc in enumerate(documents):
        
        citation_id = f"{i+1}",
        source= doc["text"],
        page=doc["page"],
        
        context += (f"{citation_id}\n"
                    f"{doc['text']}\n\n"
                    )
        citations.append({
            "id": citation_id,
            "source": source,
            "page": page
        })
        
    return context, citations
        
        
        
        
        