# Build Your Own Jarvis - Personal AI Assistant

A clean, modular Python project for building a self-hosted personal AI assistant using LLaMA, LangChain, and Pinecone vector database.

## 🚀 Features

- **Self-Hosted LLM**: Uses Mistral-7B or LLaMA models locally
- **Vector Database**: Pinecone for efficient semantic search
- **LangChain Integration**: Powerful chains for RAG (Retrieval-Augmented Generation)
- **Conversational Memory**: Maintains chat history
- **Web UI**: Streamlit-based user-friendly interface
- **Modular Architecture**: Clean separation of concerns with separate files for each function

## 📁 Project Structure

```
dilligen/
├── config.py           # Configuration and API keys
├── llm_model.py        # LLM and embeddings initialization
├── vector_db.py        # Pinecone database management
├── chain.py            # LangChain chain setup
├── chat_handler.py     # Query processing and response generation
├── utils.py            # Utility functions
├── main.py             # Streamlit chatbot UI
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── README.md           # This file
```

## 📋 Prerequisites

- Python 3.10+
- GPU (recommended) or CPU
- Pinecone account (free tier available)
- 16GB+ RAM for running LLMs

## 🔧 Installation

1. **Clone or create the project**
   ```bash
   cd dilligen
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   - The `.env` file is already configured with your Pinecone API key
   - All environment variables are ready to use

## 🚀 Running the Application

### Option 1: Streamlit Web UI (Recommended)
```bash
streamlit run main.py
```
Then open `http://localhost:8501` in your browser.

### Option 2: Command Line Interface
```python
from chat_handler import ChatHandler
from utils import print_welcome_message, format_response

handler = ChatHandler()
print_welcome_message()

while True:
    query = input("You: ")
    if query.lower() in ['quit', 'exit']:
        break
    response = handler.process_query(query)
    print(format_response(response))
```

## 📚 Usage Examples

### In Streamlit UI
1. Type your question in the input box
2. Upload documents to add to the knowledge base
3. View chat history and sources in the sidebar
4. Clear history as needed

### In Python Code
```python
from chat_handler import ChatHandler

handler = ChatHandler()

# Ask a question
response = handler.process_query("What is the capital of France?")
print(response["answer"])

# Add documents to knowledge base
handler.add_document("France is a country in Western Europe...")

# Get chat history
history = handler.get_chat_history()
```

## 🔑 Configuration

Edit the following files to customize:

- **config.py**: API keys, model names, temperature, max tokens
- **.env**: Environment-specific settings
- **chain.py**: Prompt templates and retrieval settings

## 📖 Module Descriptions

### config.py
Centralized configuration management for:
- Pinecone connection settings
- LLM parameters
- Embeddings model
- Chat parameters

### llm_model.py
Handles:
- LLM initialization (Mistral, LLaMA, etc.)
- Embeddings model setup
- Text generation
- Vector embedding creation

### vector_db.py
Manages:
- Pinecone index initialization
- Upserting vectors
- Querying similar vectors
- Index management

### chain.py
Implements:
- LangChain RetrievalQA chain
- Custom prompt templates
- Conversation memory
- Document retrieval

### chat_handler.py
Provides:
- Query processing
- Response generation
- Chat history management
- Document management

### utils.py
Contains:
- Response formatting
- Chat history I/O
- Input validation
- UI helpers

### main.py
Streamlit application with:
- Chat interface
- File upload for knowledge base
- Chat history management
- Response details display

## 🎯 Next Steps

1. Get a Pinecone API key from https://pinecone.io
2. Update `.env` with your credentials
3. Download a local LLM model (first run will auto-download)
4. Run the application
5. Start asking questions!

## ⚠️ Notes

- First run will download the LLM model (~4-7GB for Mistral-7B)
- GPU recommended for faster inference
- Pinecone free tier supports 1M vectors
- Adjust `LLM_MAX_TOKENS` and temperature for response quality

## 📝 License

This project is part of the Diligent Corporation Learning Program.

## 🤝 Support

For issues or questions, refer to:
- LangChain Docs: https://python.langchain.com/
- Pinecone Docs: https://docs.pinecone.io/
- Streamlit Docs: https://docs.streamlit.io/
