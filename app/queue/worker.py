import json
import asyncio
from aio_pika import connect_robust, IncomingMessage
from app.queue.rabbitmq import (QUEUE_NAME, RABBITMQ_URL)
from app.db.queries import get_raw_document , mark_processing_job, mark_proccessing_failure, mark_processing_complete
from app.ingestions.pipeline import pipeline_ingestion
from fastapi import HTTPException

MAX_RETRIES = 3

async def process_message(message: IncomingMessage):

    async with message.process(requeue=False):

        payload = json.loads(
            message.body.decode()
        )

        doc_id = payload["doc_id"]
        job_id= payload["job_id"]

        print(f"processing: {doc_id}")
        
        await mark_processing_job(job_id)
        
    try:

        raw_document = await get_raw_document(
            doc_id
        )

        if not raw_document:
            print("document not found")
            raise ValueError(f'document is not found')

        await pipeline_ingestion(
            raw_document
        )
        
        await mark_processing_complete(job_id)

        print(f"completed: {doc_id}")
        
    except Exception as e:
        print ('error while processing ', str(e))
        await  mark_proccessing_failure(job_id, str(e))
        raise HTTPException(status_code=500, detail=f"Failed to ingestion processing ") from e



async def start_worker():
    connection= await connect_robust(
        RABBITMQ_URL
    )
    
    channel= await connection.channel()
    await channel.set_qos(
        prefetch_count=5
    )
    queue = await channel.declare_queue(
        QUEUE_NAME,
        durable=True
    )
    
    await queue.consume(
        process_message
    )
    
    print("worker started")

    await asyncio.Future()
    
if __name__ == "__main__":
    asyncio.run(
        start_worker()
    )
    
    
    
    