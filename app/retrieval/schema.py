from pydantic import BaseModel
from typing import List, Dict, Any
from datetime import datetime


class DocumentSchema(BaseModel):
    doc_id: str
    source_type: str
    title: str
    content:str
    created_at: datetime
    