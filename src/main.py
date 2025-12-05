from fastapi import FastAPI
from src.routers.chat_router import router as chat_router

app = FastAPI(title="LLM Backend Orchestrator")

app.include_router(chat_router)

@app.get("/")
def root():
    return {"status": "running"}
