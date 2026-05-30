from app.ingestions.loader import load_pdf
from app.ingestions.chunks import chunking
from app.retrieval.indexer import index_chunks
from fastapi import HTTPException
import os
async def pipeline_ingestion(document):
    
    try:
     # Step 1: Load PDF
    #  documents = load_pdf(file_path)
    
     # Step 2: Chunking
     chunks = chunking(document)
    
    #  # Step 3: Indexing
     index_chunks(chunks, document)
          
    
     print(f"Pipeline completed for file")
    except Exception as e:
        print(f"Error processing file: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to process file ") from e
         
        
   
    
    