
from app.db.postgresql import get_pool
async def insert_raw_document(document):
    pool= await get_pool()
    
    async with pool.acquire() as conn:
        await conn.execute(
            """
            INSERT INTO raw_documents (
                doc_id,
                source_type,
                title,
                content
            )
            VALUES ($1, $2, $3, $4)
            ON CONFLICT (doc_id)
            DO NOTHING
            """,
            document.doc_id,
            document.source_type,
            document.title,
            document.content
            )
        
        
 
async def get_raw_document(doc_id:str):
    pool= await get_pool()
    
    async with pool.acquire() as conn:
        row = await conn.fetchrow(
            """
            SELECT *
            FROM raw_documents
            WHERE doc_id = $1
            """,
            doc_id
        )

        return dict(row) if row else None
    
    
    
async def insert_ingestion_job(doc_id: str, source_type: str, pipeline_version: str = "v1"):
    pool= await get_pool()
    
    async with pool.acquire() as conn:
        row= await conn.fetchrow(
            """
            INSERT INTO ingestion_jobs (
                doc_id,
                source_type,
                status,
                attempts,
                pipeline_version
            )
            VALUES ($1, $2, 'queued', 0, $3)
            RETURNING job_id, doc_id, status
            """,
            doc_id,
            source_type,
            pipeline_version
        )   
        return dict(row) if row else None     
    
    

async def mark_processing_job(job_id:int):
    pool= await get_pool()
    
    async with pool.acquire() as conn:
        await conn.execute(
            """
            UPDATE ingestion_jobs
            SET status = 'processing',
                attempts = attempts + 1,
                started_at = COALESCE(started_at, NOW()),
                updated_at = NOW()
            WHERE job_id = $1
            """,
            job_id
        )


async def mark_processing_complete(job_id:int):
    
    pool= await get_pool()
    
    async with  pool.acquire() as conn:
        
        await conn.execute(
            """
            UPDATE ingestion_jobs
            SET status ='completed',
                completed_at = NOW(),
                updated_at = NOW()
            WHERE job_id= $1    
            """,
            job_id
            
        )  
        
async def mark_proccessing_failure(job_id:int , error: str):
    
    pool= await get_pool()
    
    async with pool.acquire() as conn:
        
        await conn.execute(
            """
            UPDATE ingestion_jobs
            SET status='failed',
                error = $2,
                updated_at = NOW(),
            Where job_id =$1
            """,
            job_id,
            error
            
        )           
        
            
    
    
            