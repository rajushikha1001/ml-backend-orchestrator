import httpx
from src.config.settings import settings

async def chat_vllm(prompt: str, model: str = "mistral"):
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{settings.VLLM_URL}/generate",
            json={"prompt": prompt, "model": model, "max_tokens": 250}
        )
        return resp.json()["text"]
