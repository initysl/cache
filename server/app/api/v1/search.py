from fastapi import APIRouter,Security
from app.schemas.search import SearchRequest, SearchResponse
from app.dependencies import vector_store
from app.core.security import verify_api_key


router = APIRouter(prefix="/search", tags=["Search"])

@router.post("/", response_model=SearchResponse)
def search_document(payload: SearchRequest, api_key: str = Security(verify_api_key)):
    results = vector_store.search(
        query=payload.query,
        top_k=payload.top_k,
        where=payload.where,
        where_document=payload.where_document
    )
    return {"results": results}
