
from datetime import datetime
import uuid

def _get_document_attr(document, attr):
    if isinstance(document, dict):
        return document.get(attr)
    return getattr(document, attr, None)


def build_meta_data(document, chunk_index:int):
    
    
    meta_data={
        "doc_id": _get_document_attr(document, "doc_id"),
        "chunk_id": str(uuid.uuid4()),
        "chunk_index": chunk_index,
        "created_at": datetime.now().isoformat()
    }
  
    return meta_data