from fastapi import APIRouter
from app.data.data_loader import load_raw_data
from app.retrieval.schema import DocumentSchema
from datetime  import datetime
from app.ingestions.pipeline import pipeline_ingestion


router= APIRouter()
@router.get("/load-data/")
async def load_data():
    documents = load_raw_data()
    
    for raw_doc in documents:
        document= DocumentSchema(
            doc_id= raw_doc["doc_id"],
            source_type= raw_doc["source_type"],
            title= raw_doc["title"],
            content= raw_doc["content"],
            created_at=datetime.now().isoformat()  
        )
        
        pipeline_ingestion(document)
        
        
