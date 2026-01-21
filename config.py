# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# FIX: Removed the hyphen. It must be "qwen2.5"
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5")

# Embeddings model
EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL", "all-MiniLM-L6-v2")

# Pinecone
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "jarvis-knowledge")