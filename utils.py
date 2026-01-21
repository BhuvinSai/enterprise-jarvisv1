# utils.py
import json
from datetime import datetime

def format_response(response):
    formatted = f"""
-----------------------------------
Query: {response['query']}
-----------------------------------
Answer: {response['answer']}
-----------------------------------
Source Documents: {response['similar_docs_count']}
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
-----------------------------------
"""
    return formatted

def save_chat_history(chat_history, filename="chat_history.json"):
    with open(filename, "w") as f:
        json.dump(chat_history, f, indent=2)

def load_chat_history(filename="chat_history.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def validate_input(user_input):
    return bool(user_input and len(user_input.strip()) > 0)
