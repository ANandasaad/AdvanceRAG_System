from fastapi import FastAPI

from app.retrieval.create_collection import create_collection

from app.apis.upload_pdf import router as upload_pdf_router
from app.apis.search import router as search_router

app = FastAPI(title= "Advanced RAG System", description= "An advanced Retrieval-Augmented Generation system using FastAPI and LangChain", version= "1.0.0")

app.include_router(upload_pdf_router)
app.include_router(search_router)

@app.on_event("startup")
async def startup_event():
    create_collection()
    
    print("Startup event completed. Collection is ready.")

@app.get("/")
async def root():
    return {"message": "Welcome to the Advanced RAG System API!"}


    