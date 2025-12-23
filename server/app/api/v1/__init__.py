from fastapi import APIRouter
from app.api.v1 import ingest, search, health, documents

api_router = APIRouter()

api_router.include_router(ingest.router)
api_router.include_router(search.router)
api_router.include_router(health.router)
api_router.include_router(documents.router)