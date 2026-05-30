from fastapi import FastAPI

from app.retrieval.create_collection import create_collection
from app.apis.upload_pdf import router as upload_pdf_router
from app.apis.search import router as search_router
from app.apis.load_data import router as load_data_router
from app.db.init_db import create_table

app = FastAPI(title= "Advanced RAG System", description= "An advanced Retrieval-Augmented Generation system using FastAPI and LangChain", version= "1.0.0")

app.include_router(upload_pdf_router)
app.include_router(search_router)
app.include_router(load_data_router)


@app.on_event("startup")
async def startup_event():
    await create_table()
    print("Tables created")
    create_collection()
    print("Startup event completed. Collection is ready. Index is ready.")
    
    

@app.get("/")
async def root():
    return {"message": "Welcome to the Advanced RAG System API!"}


    