from app.ingestions.loader import load_pdf
from app.ingestions.chunks import chunking
from app.retrieval.indexer import index_chunks
from fastapi import HTTPException
import os
def pipeline_ingestion(file_path):
    
    try:
     # Step 1: Load PDF
     documents = load_pdf(file_path)
    
     # Step 2: Chunking
     chunks = chunking(documents)
    
     # Step 3: Indexing
     index_chunks(chunks)
          
    
     print(f"Pipeline completed for file: {file_path}")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to process file {file_path}") from e
         
        
   
    
    