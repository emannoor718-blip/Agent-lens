# inference.py
from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL, OLLAMA_BASE_URL, OLLAMA_MODEL


# ── 1. OpenAI Responses API (with Web Search) ────────────────
def responses_api(query: str) -> str:
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.responses.create(
        model=OPENAI_MODEL,
        tools=[{"type": "web_search_preview"}],
        input=query,
    )
    # Extract text from response output
    for item in response.output:
        if hasattr(item, "content"):
            for block in item.content:
                if hasattr(block, "text"):
                    return block.text
    return "No response."


# ── 2. OpenAI Chat Completions ───────────────────────────────
def chat_completions(query: str) -> str:
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": query}],
    )
    return response.choices[0].message.content


# ── 3. Ollama (via OpenAI-compatible endpoint) ───────────────
def ollama_chat(query: str, model: str = OLLAMA_MODEL) -> str:
    client = OpenAI(
        api_key="ollama",                # Required but ignored by Ollama
        base_url=OLLAMA_BASE_URL,
    )
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": query}],
    )
    return response.choices[0].message.content