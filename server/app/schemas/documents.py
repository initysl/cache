from pydantic import BaseModel
from typing import List, Dict, Optional

class DocumentResponse(BaseModel):
    id: str
    text: Optional[str]
    metadata: Dict

class UpdateRequest(BaseModel):
    text: Optional[str] = None
    metadata: Optional[Dict] = None

class DeleteBatchRequest(BaseModel):
    ids: List[str]

class StatsResponse(BaseModel):
    total_documents: int