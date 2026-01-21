# 🤖 Enterprise Jarvis - Secure AI Research Assistant

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![AI Model](https://img.shields.io/badge/AI-Qwen_2.5_(Local)-purple)
![Database](https://img.shields.io/badge/Vector_DB-Pinecone-green)
![Status](https://img.shields.io/badge/Status-Active-success)

**Enterprise Jarvis** is a self-hosted, secure AI assistant designed for enterprise environments. Unlike standard chatbots, Jarvis uses **RAG (Retrieval-Augmented Generation)** to ground its answers in your specific internal documents, ensuring accuracy and reducing hallucinations.

It runs the **Qwen 2.5** Large Language Model entirely locally via Ollama, ensuring that sensitive query logic remains on-premise, while leveraging **Pinecone** for scalable knowledge retrieval.

## 🚀 Key Features

* **🔒 Privacy-First Architecture:** Uses a local LLM (Qwen 2.5), so your questions never leave your machine.
* **🧠 RAG (Retrieval-Augmented Generation):** Connects the AI to a Pinecone Vector Database to answer based on *your* data, not just general knowledge.
* **⚡ High Performance:** Optimized caching strategies in Streamlit for instant model loading.
* **🎨 Enterprise UI:** A polished, professional interface built with Streamlit, featuring chat history and source citation.
* **📄 Source Transparency:** "Glass Box" AI that cites exactly which documents it used to generate an answer.

## 🛠️ Tech Stack

* **Frontend:** Streamlit (Python)
* **AI Engine:** Ollama (running Qwen 2.5)
* **Vector Database:** Pinecone (Serverless Index)
* **Orchestration:** LangChain Community & Custom Python Logic
* **Embeddings:** `all-MiniLM-L6-v2` (Sentence Transformers)

## 🔧 Installation & Setup

### 1. Prerequisites
* Python 3.10+ installed.
* [Ollama](https://ollama.com/) installed and running.
* A [Pinecone](https://www.pinecone.io/) API Key (Free Tier works).

### 2. Clone the Repository
```bash
git clone [https://github.com/BhuvinSai/enterprise-jarvisv1.git](https://github.com/BhuvinSai/enterprise-jarvisv1.git)
cd enterprise-jarvisv1
