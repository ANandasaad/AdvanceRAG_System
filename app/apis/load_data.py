from fastapi import APIRouter
from app.data.data_loader import load_raw_data
from app.retrieval.schema import DocumentSchema
from datetime  import datetime
from app.db.queries import insert_raw_document, insert_ingestion_job
from app.queue.publisher import publish_ingestion_job
from app.utils.source_parser import normalize_text
from app.utils.source_parser import parser

router= APIRouter()
@router.get("/load-data/")
async def load_data():
    documents = load_raw_data()
    
    total=0
    
    for raw_doc in documents:
        document= DocumentSchema(
            doc_id= raw_doc["doc_id"],
            source_type= raw_doc["source_type"],
            title= raw_doc["title"],
            content= raw_doc["content"]
        )
        
        data = parser(document)
        
        await insert_raw_document(document)
        
        job=await insert_ingestion_job(
            doc_id=document.doc_id,
            source_type=document.source_type,
            pipeline_version='v1'
        )
        
        job_id= job['job_id']
        
        await publish_ingestion_job(document.doc_id, job_id)
        
        
        
        total+=1
        # pipeline_ingestion(document)
        
        
    return {
        "status": "queued",
        "documents": data
    }    
        
        
