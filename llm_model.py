# llm_model.py
import ollama
from sentence_transformers import SentenceTransformer
from config import EMBEDDINGS_MODEL, OLLAMA_MODEL

class LLMModel:
    def __init__(self):
        self.model_name = OLLAMA_MODEL
        self.embedder = SentenceTransformer(EMBEDDINGS_MODEL)

    def generate_answer(self, query: str, context_texts: list) -> str:
        """
        Constructs a prompt with context and gets answer from Ollama
        """
        context_block = "\n".join(context_texts)
        
        # FIX: Added strict formatting instructions
        prompt = f"""You are a helpful enterprise assistant. Use the context below to answer the question.
        
        STRICT FORMATTING RULES:
        1. Use bullet points for lists.
        2. Keep paragraphs short.
        3. Use bold text for key terms.
        
Context:
{context_block}

Question: {query}

Answer:"""
        
        try:
            response = ollama.generate(model=self.model_name, prompt=prompt)
            return response['response']
        except Exception as e:
            return f"Error communicating with Ollama: {e}"

    def embed_text(self, text):
        try:
            return self.embedder.encode(text).tolist()
        except Exception as e:
            print(f"Embedding error: {e}")
            return []