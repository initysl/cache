from fastapi import APIRouter, HTTPException, Security
from app.schemas.documents import DocumentResponse, UpdateRequest, DeleteBatchRequest, StatsResponse
from app.dependencies import vector_store
from app.core.security import verify_api_key

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.get("/{id}", response_model=DocumentResponse)
def get_document(id: str, api_key: str = Security(verify_api_key)):
    doc = vector_store.get_by_id(id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

@router.put("/{id}")
def update_document(id: str, payload: UpdateRequest):
    vector_store.update(id, text=payload.text, metadata=payload.metadata)
    return {"message": "Document updated"}

@router.delete("/{id}")
def delete_document(id: str):
    vector_store.delete(id)
    return {"message": "Document deleted"}

@router.post("/batch/delete")
def delete_documents_batch(payload: DeleteBatchRequest):
    vector_store.delete_batch(payload.ids)
    return {"message": f"Deleted {len(payload.ids)} documents"}

@router.get("/stats/count", response_model=StatsResponse)
def get_stats():
    return {"total_documents": vector_store.count()}

@router.delete("/clear/all")
def clear_all():
    vector_store.clear()
    return {"message": "All documents cleared"}