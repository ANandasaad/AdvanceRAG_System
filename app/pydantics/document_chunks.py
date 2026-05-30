from pydantic import BaseModel, ConfigDict, Field
from typing import List, Dict


class RawDocument(BaseModel):
    doc_id: str
    source_type: str
    title:str
    content : str
    
    model_config = ConfigDict(extra= 'forbid')
    
class Section(BaseModel):
    section_title:str
    content: str
    
    model_config = ConfigDict(extra='forbid')
    
class Entity(BaseModel):
    text: str
    label: str
    
    model_config = ConfigDict(extra='forbid')
    
class ChunkRecord(BaseModel):
    chunk_id: str
    doc_id: str
    source_type: str
    title:str
    section_title:str
    chunk_index: int
    chunk_text: str
    summary:str
    entities: List[Entity]=  Field(default_factory=list)  
    hypothetical_questions : List[str] = Field(default_factory=list)
    
    model_config= ConfigDict(extra='forbid')        