import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    VLLM_URL = os.getenv("VLLM_URL", "http://localhost:8001")
    OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

settings = Settings()
