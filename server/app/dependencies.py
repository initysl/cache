from app.services.embedding import EmbeddingService
from app.services.vector_store import VectorStore

embedding_service = EmbeddingService()
vector_store = VectorStore(embedding_service=embedding_service)