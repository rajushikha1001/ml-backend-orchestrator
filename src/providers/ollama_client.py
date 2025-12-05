import httpx
from src.config.settings import settings

async def chat_ollama(prompt: str, model: str = "llama3"):
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{settings.OLLAMA_URL}/api/chat",
            json={"model": model, "messages": [{"role": "user", "content": prompt}]}
        )
        data = resp.json()
        return data["message"]["content"]
