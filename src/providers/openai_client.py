import openai
from src.config.settings import settings

openai.api_key = settings.OPENAI_API_KEY

async def chat_openai(prompt: str, model: str = "gpt-4o-mini"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
