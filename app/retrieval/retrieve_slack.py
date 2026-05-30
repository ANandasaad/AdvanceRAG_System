from fastapi import HTTPException
from app.retrieval.search import search
async def retrieve_slack(query:str):
    try:
        retrieve_result= await search(query)
        return retrieve_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to search query slack") from e

        
            