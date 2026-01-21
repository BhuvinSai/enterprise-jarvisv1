# main.py
import streamlit as st
import time
from chat_handler import ChatHandler

# 1. Page Configuration
st.set_page_config(
    page_title="Diligent Enterprise Jarvis",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS for Professional Look
st.markdown("""
<style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .stMarkdown h1 {
        color: #B91C1C;
    }
</style>
""", unsafe_allow_html=True)

# 3. CACHING: This is the specific fix for speed!
#    It prevents reloading the AI models on every page refresh.
@st.cache_resource(show_spinner="Loading Jarvis Brain...")
def get_cached_handler():
    return ChatHandler()

# 4. Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=50)
    st.title("Settings")
    st.caption(f"Brain: Qwen 2.5 (Local)")
    
    st.markdown("---")
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# 5. Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize the handler using the CACHED function
try:
    if "chat_handler" not in st.session_state:
        st.session_state.chat_handler = get_cached_handler()
except Exception as e:
    st.error(f"Failed to load Jarvis: {e}")
    st.stop()

# 6. Header
st.title("🤖 Diligent Enterprise Jarvis")
st.markdown("### Your Secure AI Research Assistant")

# 7. Display Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("sources"):
            with st.expander("📚 View Source Documents"):
                for doc in msg["sources"]:
                    st.info(doc)

# 8. Chat Input & Processing
if prompt := st.chat_input("Ask Jarvis a question..."):
    # Add User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Analyzing knowledge base..."):
            try:
                # Call the backend
                response_data = st.session_state.chat_handler.chat(prompt)
                
                # Handle response
                if isinstance(response_data, str):
                    answer = response_data
                    sources = []
                else:
                    answer = response_data.get("answer", "No answer generated.")
                    sources = response_data.get("source_documents", [])

                # Simulate typing effect
                full_response = ""
                for chunk in answer.split():
                    full_response += chunk + " "
                    time.sleep(0.02)
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
                
                # Save to history
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": full_response,
                    "sources": sources
                })
                
                # Show sources
                if sources:
                    with st.expander("📚 View Source Documents"):
                        for doc in sources:
                            st.info(doc)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")