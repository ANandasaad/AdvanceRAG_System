from app.db.postgresql import get_pool
from fastapi import HTTPException
async def create_table():
 try:
        
    pool= await get_pool()
    async with pool.acquire() as conn:
        await conn.execute(
            """
            CREATE TABLE IF NOT EXISTS raw_documents (

                id BIGSERIAL PRIMARY KEY,

                doc_id TEXT UNIQUE NOT NULL,

                source_type TEXT NOT NULL,

                title TEXT NOT NULL,

                content TEXT NOT NULL,

                created_at TIMESTAMP DEFAULT NOW(),

                updated_at TIMESTAMP DEFAULT NOW()
            );
            
            """
            
        )
        
        await conn.execute(
            """
            CREATE TABLE IF NOT EXISTS ingestion_jobs (

                job_id BIGSERIAL PRIMARY KEY,
                doc_id TEXT NOT NULL,
                source_type TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'queued',
                attempts INTEGER NOT NULL DEFAULT 0,
                error TEXT,
                pipeline_version TEXT NOT NULL DEFAULT 'v1',
                created_at TIMESTAMP NOT NULL DEFAULT NOW(),
                updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
                started_at TIMESTAMP,
                completed_at TIMESTAMP
            );
            
            CREATE INDEX IF NOT EXISTS idx_ingestion_jobs_status ON ingestion_jobs(status);
            CREATE INDEX IF NOT EXISTS idx_ingestion_jobs_doc_id ON ingestion_jobs(doc_id);
            """
        )
        
        await conn.execute(
            """
            CREATE TABLE IF NOT EXISTS documents_chunks (
                
                chunk_id TEXT PRIMARY KEY,
                doc_id TEXT NOT NULL,
                source_type TEXT NOT NULL,
                title TEXT NOT NULL,
                section_title TEXT NOT NULL,
                chunk_index INT NOT NULL,
                chunk_text TEXT NOT NULL,
                summary TEXT NOT NULL,
                entites JSONB NOT NULL,
                hypothetical_questions JSONB NOT NULL,
                created_at TIMESTAMP NOT NULL DEFAULT NOW()
                
            )
            """
            
        )
    print("tables created")
    
 except Exception as e:
       print(f"Error occurred during table creation: {e}")
       raise HTTPException(status_code=500, detail="Failed to created tables") from e