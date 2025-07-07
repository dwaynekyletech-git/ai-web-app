from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import litellm
import os

router = APIRouter()

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    model: Optional[str] = "gpt-3.5-turbo"
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 1000

class ChatResponse(BaseModel):
    message: str
    model: str
    usage: Optional[dict] = None

@router.post("/chat", response_model=ChatResponse)
async def chat_completion(request: ChatRequest):
    try:
        # Convert messages to LiteLLM format
        messages = [{"role": msg.role, "content": msg.content} for msg in request.messages]
        
        # Make API call using LiteLLM
        response = litellm.completion(
            model=request.model,
            messages=messages,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        
        return ChatResponse(
            message=response.choices[0].message.content,
            model=response.model,
            usage=response.usage.dict() if response.usage else None
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI service error: {str(e)}")

@router.get("/models")
async def get_available_models():
    # Return list of available models
    return {
        "models": [
            "gpt-3.5-turbo",
            "gpt-4",
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307"
        ]
    }