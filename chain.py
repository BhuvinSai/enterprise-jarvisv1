# chain.py
class ChainSetup:
    def __init__(self, llm_model, vector_db):
        self.llm_model = llm_model
        self.vector_db = vector_db

    def query(self, query_text):
        # 1. Turn question into numbers (vector)
        query_vector = self.llm_model.embed_text(query_text)

        # 2. Search Pinecone for similar text
        search_results = self.vector_db.query(query_vector, top_k=3)
        
        # 3. Extract the actual text from the search results
        retrieved_texts = []
        if hasattr(search_results, 'matches'):
            for match in search_results.matches:
                if match.metadata and 'text' in match.metadata:
                    retrieved_texts.append(match.metadata['text'])

        # 4. Ask the LLM (Ollama) to answer using that text
        response = self.llm_model.generate_answer(query_text, retrieved_texts)
        return response