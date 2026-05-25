import os
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException
from app.ingestions.pipeline import pipeline_ingestion


router = APIRouter()

UPLOAD_DIR = "uploaded_pdfs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
@router.post("/upload-pdf/")
async def upload_pdf(file:UploadFile = File(...)):
    file_path= os.path.join(UPLOAD_DIR, file.filename)
    try:
      with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        pipeline_ingestion(file_path)
      return {"filename": file.filename, "message": "PDF uploaded successfully"}    
    except Exception as e:
      raise HTTPException(status_code=500, detail=f"Failed to upload PDF: {str(e)}") from e
      

    