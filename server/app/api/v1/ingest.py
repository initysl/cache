from fastapi import APIRouter, Security
from app.schemas.ingest import IngestRequest, IngestResponse
from app.dependencies import vector_store
from app.core.security import verify_api_key

router = APIRouter(prefix="/ingest", tags=["Ingest"])

@router.post("/", response_model=IngestResponse)
def ingest_document(payload: IngestRequest, api_key: str = Security(verify_api_key),):
    # Handle batch or single
    if isinstance(payload.text, list):
        vector_ids = vector_store.add_batch(
            texts=payload.text,
            metadatas=[payload.metadata] * len(payload.text) if payload.metadata else None
        )
        return {"id": vector_ids}
    else:
        vector_id = vector_store.add(
            text=payload.text,
            metadata=payload.metadata
        )
        return {"id": vector_id}
