import aio_pika
RABBITMQ_URL = "amqp://guest:guest@localhost/"
QUEUE_NAME = "document_ingestion"

async def get_rabbitmq_channel():
    connection= await aio_pika.connect_robust(
        RABBITMQ_URL
    )
    
    channel= await connection.channel()
    
    await channel.set_qos(
        prefetch_count=10
    )
    
    await channel.declare_queue(
        QUEUE_NAME,
        durable=True
    )
    
    return channel


