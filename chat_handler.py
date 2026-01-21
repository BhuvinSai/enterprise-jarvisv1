# chat_handler.py
from llm_model import LLMModel
from vector_db import VectorDB
from chain import ChainSetup

class ChatHandler:
    def __init__(self):
        try:
            self.llm_model = LLMModel()
        except Exception as e:
            print(f"Error initializing LLM model: {e}")
            raise e

        try:
            self.vector_db = VectorDB()
        except Exception as e:
            print(f"Error initializing VectorDB: {e}")
            raise e

        try:
            self.chain = ChainSetup(self.llm_model, self.vector_db)
        except Exception as e:
            print(f"Error initializing ChainSetup: {e}")
            raise e

    def chat(self, query):
        if not query.strip():
            return "Please enter a question."
        try:
            response = self.chain.query(query)
            return response
        except Exception as e:
            print(f"Error during chat query: {e}")
            return "Sorry, something went wrong while processing your request."
