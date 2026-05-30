import os
import asyncpg

from dotenv import load_dotenv

load_dotenv()

DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_USERNAME=os.getenv("DB_USERNAME")
DB_NAME=os.getenv("DB_NAME")
DB_PASSWORD=os.getenv("DB_PASSWORD")


pg_pool=None

async def get_pool():
    global pg_pool
    
    if pg_pool is None:
        pg_pool = await asyncpg.create_pool(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USERNAME,
            password=DB_PASSWORD,
            database=DB_NAME,
            min_size=5,
            max_size=20
        )
        
        print("PG pool created successfully")
        
    return pg_pool    
        
        
        