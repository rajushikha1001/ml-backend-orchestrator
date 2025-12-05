from fastapi import APIRouter
from src.schemas import ChatRequest, ChatResponse
from src.providers.openai_client import chat_openai
from src.providers.anthropic_client import chat_anthropic
from src.providers.ollama_client import chat_ollama
from src.providers.vllm_client import chat_vllm

router = APIRouter(prefix="/api/chat")

@router.post("/openai", response_model=ChatResponse)
async def chat_with_openai(req: ChatRequest):
    result = await chat_openai(req.prompt, req.model)
    return ChatResponse(response=result)

@router.post("/anthropic", response_model=ChatResponse)
async def chat_with_anthropic(req: ChatRequest):
    result = await chat_anthropic(req.prompt, req.model)
    return ChatResponse(response=result)

@router.post("/ollama", response_model=ChatResponse)
async def chat_with_ollama(req: ChatRequest):
    result = await chat_ollama(req.prompt, req.model)
    return ChatResponse(response=result)

@router.post("/vllm", response_model=ChatResponse)
async def chat_with_vllm(req: ChatRequest):
    result = await chat_vllm(req.prompt, req.model)
    return ChatResponse(response=result)
