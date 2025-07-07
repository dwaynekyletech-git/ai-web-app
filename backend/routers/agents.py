from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from database.supabase import get_supabase_client
from utils.ai_client import ai_client

router = APIRouter()

class AgentCreate(BaseModel):
    name: str
    description: Optional[str] = None
    system_prompt: str
    model: str = "gpt-3.5-turbo"
    temperature: float = 0.7
    max_tokens: int = 1000

class AgentUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    system_prompt: Optional[str] = None
    model: Optional[str] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    is_active: Optional[bool] = None

class AgentResponse(BaseModel):
    id: str
    name: str
    description: Optional[str]
    system_prompt: str
    model: str
    temperature: float
    max_tokens: int
    is_active: bool
    created_at: str
    updated_at: str

class AgentChatRequest(BaseModel):
    message: str
    conversation_context: Optional[List[dict]] = []

class AgentChatResponse(BaseModel):
    response: str
    agent_id: str
    model: str
    usage: Optional[dict] = None

@router.post("/", response_model=AgentResponse)
async def create_agent(agent: AgentCreate):
    """Create a new AI agent"""
    # TODO: Implement with proper user authentication
    # This is a placeholder implementation
    supabase = get_supabase_client()
    
    try:
        result = supabase.table("ai_agents").insert({
            "name": agent.name,
            "description": agent.description,
            "system_prompt": agent.system_prompt,
            "model": agent.model,
            "temperature": agent.temperature,
            "max_tokens": agent.max_tokens,
            "user_id": "placeholder_user_id"  # TODO: Get from auth
        }).execute()
        
        return AgentResponse(**result.data[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create agent: {str(e)}")

@router.get("/", response_model=List[AgentResponse])
async def list_agents():
    """List all AI agents for the current user"""
    # TODO: Implement with proper user authentication
    supabase = get_supabase_client()
    
    try:
        result = supabase.table("ai_agents").select("*").eq("user_id", "placeholder_user_id").execute()
        return [AgentResponse(**agent) for agent in result.data]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list agents: {str(e)}")

@router.get("/{agent_id}", response_model=AgentResponse)
async def get_agent(agent_id: str):
    """Get a specific AI agent"""
    supabase = get_supabase_client()
    
    try:
        result = supabase.table("ai_agents").select("*").eq("id", agent_id).execute()
        
        if not result.data:
            raise HTTPException(status_code=404, detail="Agent not found")
            
        return AgentResponse(**result.data[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get agent: {str(e)}")

@router.put("/{agent_id}", response_model=AgentResponse)
async def update_agent(agent_id: str, agent_update: AgentUpdate):
    """Update an AI agent"""
    supabase = get_supabase_client()
    
    try:
        update_data = {k: v for k, v in agent_update.dict().items() if v is not None}
        
        result = supabase.table("ai_agents").update(update_data).eq("id", agent_id).execute()
        
        if not result.data:
            raise HTTPException(status_code=404, detail="Agent not found")
            
        return AgentResponse(**result.data[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update agent: {str(e)}")

@router.delete("/{agent_id}")
async def delete_agent(agent_id: str):
    """Delete an AI agent"""
    supabase = get_supabase_client()
    
    try:
        result = supabase.table("ai_agents").delete().eq("id", agent_id).execute()
        
        if not result.data:
            raise HTTPException(status_code=404, detail="Agent not found")
            
        return {"message": "Agent deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete agent: {str(e)}")

@router.post("/{agent_id}/chat", response_model=AgentChatResponse)
async def chat_with_agent(agent_id: str, request: AgentChatRequest):
    """Chat with a specific AI agent"""
    supabase = get_supabase_client()
    
    try:
        # Get agent configuration
        agent_result = supabase.table("ai_agents").select("*").eq("id", agent_id).execute()
        
        if not agent_result.data:
            raise HTTPException(status_code=404, detail="Agent not found")
            
        agent = agent_result.data[0]
        
        if not agent["is_active"]:
            raise HTTPException(status_code=400, detail="Agent is not active")
        
        # Prepare messages with system prompt
        messages = [{"role": "system", "content": agent["system_prompt"]}]
        
        # Add conversation context if provided
        if request.conversation_context:
            messages.extend(request.conversation_context)
            
        # Add user message
        messages.append({"role": "user", "content": request.message})
        
        # Get AI response
        response = await ai_client.chat_completion(
            messages=messages,
            model=agent["model"],
            temperature=agent["temperature"],
            max_tokens=agent["max_tokens"]
        )
        
        return AgentChatResponse(
            response=response["content"],
            agent_id=agent_id,
            model=response["model"],
            usage=response["usage"]
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to chat with agent: {str(e)}")

@router.get("/{agent_id}/test")
async def test_agent(agent_id: str):
    """Test an AI agent with a simple message"""
    return await chat_with_agent(agent_id, AgentChatRequest(
        message="Hello! Please introduce yourself and describe your capabilities.",
        conversation_context=[]
    ))