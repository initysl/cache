import os
from huggingface_hub import InferenceClient


class EmbeddingService:
    """Load embedding model"""
    def __init__(self) -> None:
        # Store client as instance variable
        self.client = InferenceClient(
            provider="hf-inference",
            api_key=os.getenv("HF_TOKEN")
        )

        self.model = "sentence-transformers/all-MiniLM-L6-v2"

    def embed(self, text: str):
        """Generate embedding"""
        embedding = self.client.feature_extraction(text, model=self.model)
        return embedding  