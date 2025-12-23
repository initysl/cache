from typing import List, Dict, Optional
import chromadb
import uuid


class VectorStore:
    def __init__(self, embedding_service, collection_name: str = "vectors", persist_directory: str = "./chroma_db" ):
        """
        Initialize VectorStore with ChromaDB.
        Args:
            embedding_service: Instance of EmbeddingService
            collection_name: Name of the ChromaDB collection
            persist_directory: Directory for persistent storage
        """
        self.embedding_service = embedding_service
        
        # Initialize ChromaDB persistent client // check for production use
        self.client = chromadb.PersistentClient(path=persist_directory)
        
        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            #hnsw:is the nearest-neighbor search algorithm | space:defines the distance metric. 
            metadata={"hnsw:space": "cosine"}  
        )

    def add(self, text: str, metadata: Optional[Dict] = None, vector_id: Optional[str] = None) -> str:
        """
        Add a text with optional metadata to the vector store.
        Args:
            text: Text content to embed and store
            metadata: Optional metadata dictionary
            vector_id: Optional custom ID (generates UUID if not provided)
        Returns:
            The vector ID (str)
        """
        if not vector_id:
            vector_id = str(uuid.uuid4())
        
        # Generate embedding
        embedding = self.embedding_service.embed(text)
        
        # Add to collection
        self.collection.add(
            ids=[vector_id],
            embeddings=[embedding],
            metadatas=[metadata or {}],
            documents=[text]
        )
        
        return vector_id
    
    def add_batch(self, texts: List[str], metadatas: Optional[List[Dict]] = None, vector_ids: Optional[List[str]] = None) -> List[str]:
        """
        Add multiple texts in batch for better performance.
        Args:
            texts: List of text contents
            metadatas: Optional list of metadata dicts
            vector_ids: Optional list of custom IDs
        
        Returns:
            List of vector IDs
        """
        if not vector_ids:
         vector_ids = [str(uuid.uuid4()) for _ in texts]
    
        # Don't pass empty metadata dicts - pass None instead
        if metadatas and all(metadatas):  # Check if metadatas exist and are non-empty
          metadata_param = metadatas
        else:
          metadata_param = None
    
        # Generate embeddings in batch
        embeddings = [self.embedding_service.embed(text) for text in texts]
    
        # Add batch to collection
        if metadata_param:
            self.collection.add(
                ids=vector_ids,
                embeddings=embeddings,
                metadatas=metadata_param, # type: ignore
                documents=texts
            )
        else:
            self.collection.add(
            ids=vector_ids,
            embeddings=embeddings,
            documents=texts
        )
        
        return vector_ids
        
    def search(self, query: str, top_k: int = 5, where: Optional[Dict] = None, where_document: Optional[Dict] = None) -> List[Dict]:
        """
        Search for top_k most similar vectors to the query.
        Args:
            query: Search query text
            top_k: Number of results to return
            where: Optional metadata filter (e.g., {"category": "news"})
            where_document: Optional document content filter
        Returns:
            List of dicts with id, text, metadata, and distance
        """
        # Generate query embedding
        query_embedding = self.embedding_service.embed(query)
        
        # Query collection
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=where,
            where_document=where_document
        )
        
        # Format results
        hits = []
        if results["ids"] and results["ids"][0]:
            for i in range(len(results["ids"][0])):
                hits.append({
                    "id": results["ids"][0][i],
                    "text": results["documents"][0][i] if results["documents"] else None,
                    "metadata": results["metadatas"][0][i] if results["metadatas"] else {},
                    "distance": results["distances"][0][i] if results["distances"] else None
                })
        
        return hits
    
    def get_by_id(self, vector_id: str) -> Optional[Dict]:
        """
        Retrieve a specific vector by its ID.
        Args:
            vector_id: The vector ID to retrieve
        Returns:
            Dict with id, text, metadata, or None if not found
        """
        try:
            result = self.collection.get(
                ids=[vector_id],
                include=["documents", "metadatas", "embeddings"]
            )
            
            if result["ids"]:
                return {
                    "id": result["ids"][0],
                    "text": result["documents"][0] if result["documents"] else None,
                    "metadata": result["metadatas"][0] if result["metadatas"] else {},
                }
            return None
        except Exception:
            return None
    
    def update(self, vector_id: str, text: Optional[str] = None, metadata: Optional[Dict] = None):
        """
        Update an existing vector's text and/or metadata.
        Args:
            vector_id: ID of the vector to update
            text: New text content (will regenerate embedding)
            metadata: New metadata
        """
        update_params = {"ids": [vector_id]}
        
        if text is not None:
            embedding = self.embedding_service.embed(text)
            update_params["embeddings"] = [embedding]
            update_params["documents"] = [text]
        
        if metadata is not None:
            update_params["metadatas"] = [metadata] # type: ignore
        
        self.collection.update(**update_params) # type: ignore
    
    def delete(self, vector_id: str):
        """
        Delete a vector by its ID.
        
        Args:
            vector_id: The vector ID to delete
        """
        self.collection.delete(ids=[vector_id])
    
    def delete_batch(self, vector_ids: List[str]):
        """
        Delete multiple vectors by their IDs.
        Args:
            vector_ids: List of vector IDs to delete
        """
        self.collection.delete(ids=vector_ids)
    
    def count(self) -> int:
        """
        Get the total number of vectors in the collection.
        Returns:
            Count of vectors
        """
        return self.collection.count()
    
    def clear(self):
        """
        Delete all vectors from the collection.
        """
        # Delete and recreate collection
        self.client.delete_collection(name=self.collection.name)
        self.collection = self.client.get_or_create_collection(
            name=self.collection.name,
            metadata={"hnsw:space": "cosine"}
        )

