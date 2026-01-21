# vector_db.py
import os
import time
from pinecone import Pinecone, ServerlessSpec
from config import PINECONE_API_KEY, PINECONE_INDEX_NAME

class VectorDB:
    def __init__(self):
        if not PINECONE_API_KEY:
            raise ValueError("PINECONE_API_KEY is missing in .env file")

        # Initialize Pinecone (v3 style)
        try:
            self.pc = Pinecone(api_key=PINECONE_API_KEY)
        except Exception as e:
            raise RuntimeError(f"Failed to connect to Pinecone. Check your API Key. Error: {e}")

        self.index_name = PINECONE_INDEX_NAME

        # Create Index if it doesn't exist
        existing_indexes = [i.name for i in self.pc.list_indexes()]
        if self.index_name not in existing_indexes:
            try:
                self.pc.create_index(
                    name=self.index_name,
                    dimension=384,  # Standard for all-MiniLM-L6-v2
                    metric="cosine",
                    spec=ServerlessSpec(cloud="aws", region="us-east-1")
                )
                # Wait a moment for index to be ready
                time.sleep(2)
            except Exception as e:
                print(f"Index creation warning: {e}")

        self.index = self.pc.Index(self.index_name)

    def upsert(self, vectors):
        self.index.upsert(vectors=vectors)

    def query(self, vector, top_k=3):
        return self.index.query(
            vector=vector,
            top_k=top_k,
            include_metadata=True
        )