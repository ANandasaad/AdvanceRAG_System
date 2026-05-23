from fastapi import APIRouter 
from app.retrieval.search import search


router= APIRouter()

@router.get("/search/")
async def search_doc(query:str):
    
    results= await search(query)
    response= []
    for result in results.points:
         response.append({
            "text": result.payload["text"],
        })
         
    return {"results": results}     
    
    
    

    
