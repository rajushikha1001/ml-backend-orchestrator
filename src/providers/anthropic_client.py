from anthropic import Anthropic
from src.config.settings import settings

client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)

async def chat_anthropic(prompt: str, model: str = "claude-3-haiku-20240307"):
    response = client.messages.create(
        model=model,
        max_tokens=400,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text
