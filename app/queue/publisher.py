from app.queue.rabbitmq import (get_rabbitmq_channel , QUEUE_NAME)
import json
import aio_pika

async def publish_ingestion_job(doc_id:str, job_id:int):
    channel = await get_rabbitmq_channel()
    
    message_body= json.dumps({
        "doc_id": doc_id, 
        "job_id": job_id
           
    }).encode()
    
    message= aio_pika.Message(body=message_body, delivery_mode= aio_pika.DeliveryMode.PERSISTENT)
    
    await channel.default_exchange.publish(
        message=message,
        routing_key=QUEUE_NAME
    )
    
    
    print("doc_id", doc_id)