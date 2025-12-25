from fastapi import APIRouter, HTTPException, Depends
from app.schemas.documents import DocumentResponse, UpdateRequest, DeleteBatchRequest, StatsResponse
from app.dependencies import vector_store
from app.core.security import verify_api_key
from app.services.vector_store import VectorStoreError
from app.core.rate_limiter import rate_limit
import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/documents", 
    tags=["documents"],
    dependencies=[Depends(rate_limit), Depends(verify_api_key)] 
)


@router.get("/{id}", response_model=DocumentResponse)
def get_document(id: str):
    try:
        logger.info(f"Retrieving document: {id}")
        doc = vector_store.get_by_id(id)
        if not doc:
            logger.warning(f"Document not found: {id}")
            raise HTTPException(status_code=404, detail="Document not found")
        logger.info(f"Successfully retrieved document: {id}")
        return doc
    except VectorStoreError as e:
        logger.error(f"VectorStore error when retrieving document {id}: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(f"Unexpected error when retrieving document {id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put("/{id}")
def update_document(id: str, payload: UpdateRequest):
    try:
        logger.info(f"Updating document: {id}")
        vector_store.update(id, text=payload.text, metadata=payload.metadata)
        logger.info(f"Document updated succesfully: {id}")
        return {"message": "Document updated"}
    except VectorStoreError as e:
        logger.error(f"VectorStore error when updating document {id}: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(f"Unexpected error when updating document {id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/{id}")
def delete_document(id: str):
    try:
        logger.info(f"Deleting document: {id}")
        vector_store.delete(id)
        logger.info(f"Successfully deleted document: {id}")
        return {"message": "Document deleted"}
    except VectorStoreError as e:
        logger.error(f"VectorStore error when deleting document {id}: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(f"Unexpected error when deleting document {id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    

@router.post("/batch/delete")
def delete_documents_batch(payload: DeleteBatchRequest):
    try:
        logger.info(f"Batch delete request: {len(payload.ids)} document(s)")
        vector_store.delete_batch(payload.ids)
        logger.info(f"Successfully deleted {len(payload.ids)} documents")
        return {"message": f"Deleted {len(payload.ids)} documents"}
    except VectorStoreError as e:
        logger.error(f"VectorStore error during batch delete: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(f"Unexpected error during batch delete: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/stats", response_model=StatsResponse)
def get_stats():
    try:
        logger.info("Stats request received")
        count = vector_store.count()
        logger.info(f"Total documents in collection: {count}")
        return {"total_documents": count}
    except VectorStoreError as e:
        logger.error(f"VectorStore error retrieving stats: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(f"Unexpected error retrieving stats: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/clear/all")
def clear_all():
    try:
        logger.warning("Clear all request received - this will delete all documents")
        vector_store.clear()
        logger.warning("Successfully cleared all documents from collection")
        return {"message": "All documents cleared"}
    except VectorStoreError as e:
        logger.error(f"VectorStore error during clear all: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(f"Unexpected error during clear all: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")