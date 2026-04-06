# app.py
import streamlit as st
from inference import responses_api, chat_completions, ollama_chat
from config import OLLAMA_MODEL

st.set_page_config(page_title="AgentLens", page_icon="🔍")

st.title("🔍 AgentLens")
st.caption("AI Assistant — OpenAI Responses API | Chat Completions | Ollama")
st.divider()

# ── Mode Selector ────────────────────────────────────────────
mode = st.radio(
    "Select Mode:",
    ["🌐 Responses API (Web Search)", "💬 Chat Completions", "🦙 Ollama (Local)"],
    horizontal=True,
)

# ── Ollama model name input (only shown for Ollama mode) ─────
if "Ollama" in mode:
    ollama_model = st.text_input("Ollama Model Name:", value=OLLAMA_MODEL)

# ── Query Input ──────────────────────────────────────────────
query = st.text_area("Enter your query:", height=120, placeholder="Ask anything...")

# ── Run Button ───────────────────────────────────────────────
if st.button("🚀 Run", type="primary", use_container_width=True):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        with st.spinner("Thinking..."):
            try:
                if "Responses" in mode:
                    result = responses_api(query)
                elif "Chat" in mode:
                    result = chat_completions(query)
                else:
                    result = ollama_chat(query, ollama_model)

                st.markdown("### Response")
                st.markdown(result)

            except Exception as e:
                st.error(f"Error: {e}")