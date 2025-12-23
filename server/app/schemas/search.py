from typing import Dict, List, Optional
from pydantic import BaseModel


class SearchRequest(BaseModel):
    query: str
    top_k: int = 5
    where: Optional[Dict] = None
    where_document: Optional[Dict] = None


class SearchResult(BaseModel):
    id: str
    text: Optional[str]
    metadata: Dict
    distance: Optional[float]


class SearchResponse(BaseModel):
    results: List[SearchResult]
