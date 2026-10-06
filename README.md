# 🔍 AgentLens
### AI-Powered LLM Assistant — OpenAI Responses API + Chat Completions + Ollama

> A simple AI assistant that lets you switch between OpenAI Responses API (with web search), Chat Completions, and local Ollama models — all from one clean Streamlit UI.

---

## 🚀 Features

- 🌐 **OpenAI Responses API** — with real-time web search tool
- 💬 **Chat Completions API** — standard GPT conversation
- 🦙 **Ollama (Local Models)** — run LLMs locally, no API key needed
- 🔀 **Switch between all 3 modes** from the UI
- ⚡ Built with OpenAI Python SDK

---

## 📁 Project Structure

```
Agent-lens/
├── app.py          # Streamlit UI
├── inference.py    # All 3 inference functions
├── config.py       # API keys & model settings
├── .env            # Your API keys (never commit this!)
├── .gitignore      # Ignores .env and cache files
└── requirements.txt
```

---

## ⚙️ Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/emannoor718-blip/Agent-lens.git
cd Agent-lens
```

### 2. Install dependencies
```bash
uv add openai streamlit python-dotenv
```

### 3. Add your API key
Create a `.env` file:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. (Optional) Setup Ollama for local models
```bash
ollama pull llama3.2
ollama serve
```

### 5. Run the app
```bash
uv run streamlit run app.py
```

Open browser at: **http://localhost:8501**

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| OpenAI Python SDK | API client for OpenAI & Ollama |
| OpenAI Responses API | Web-search augmented responses |
| Chat Completions API | Standard GPT chat |
| Ollama | Local open-source LLMs |
| Streamlit | Web UI |
| python-dotenv | API key management |
| Python 3.10+ via uv | Runtime & package manager |

---

## 📸 Usage

1. Open the app
2. Select a mode — **Responses API**, **Chat Completions**, or **Ollama**
3. Type your query
4. Click **Run** and get your response

---

## ⚠️ Important

- Never commit your `.env` file — it contains your API key
- Ollama mode works **completely free** with no API key
- Make sure `ollama serve` is running before using Ollama mode

---

*Mid-Term Project — SAI AI Engineering | NAVTTC | Corvit Systems | Digital Pakistan*
