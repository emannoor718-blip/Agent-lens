# config.py
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL   = "gpt-4o"
OLLAMA_BASE_URL = "http://localhost:11434/v1"  # OpenAI-compatible endpoint
OLLAMA_MODEL   = "llama3.2"  # Change to any model you have pulled