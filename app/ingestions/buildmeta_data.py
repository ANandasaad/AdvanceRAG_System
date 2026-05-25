
from pathlib import Path
from datetime import datetime
import uuid
def build_meta_data(file_path:str, chunk_index:int):
    
    path= Path(file_path)
    
    meta_data={
        "chunk_id": str(uuid.uuid4()),
        "doc_type": path.suffix.replace(".",""),
        "chunk_index": chunk_index,
        "created_at": datetime.now().isoformat()
    }
  
    return meta_data