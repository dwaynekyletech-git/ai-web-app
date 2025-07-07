import litellm
import os
from typing import List, Dict, Optional
from dotenv import load_dotenv

load_dotenv()

# Configure LiteLLM
litellm.set_verbose = False

class AIClient:
    def __init__(self):
        self.setup_api_keys()
    
    def setup_api_keys(self):
        """Setup API keys for different providers"""
        # OpenAI
        if os.getenv("OPENAI_API_KEY"):
            os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
        
        # Anthropic
        if os.getenv("ANTHROPIC_API_KEY"):
            os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")
    
    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "gpt-3.5-turbo",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs
    ) -> Dict:
        """
        Generate chat completion using LiteLLM
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: Model name (e.g., 'gpt-3.5-turbo', 'claude-3-sonnet-20240229')
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            
        Returns:
            Dictionary containing response and metadata
        """
        try:
            response = litellm.completion(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                **kwargs
            )
            
            return {
                "content": response.choices[0].message.content,
                "model": response.model,
                "usage": {
                    "prompt_tokens": response.usage.prompt_tokens,
                    "completion_tokens": response.usage.completion_tokens,
                    "total_tokens": response.usage.total_tokens
                } if response.usage else None,
                "finish_reason": response.choices[0].finish_reason
            }
        except Exception as e:
            raise Exception(f"AI completion failed: {str(e)}")
    
    async def embedding(
        self,
        text: str,
        model: str = "text-embedding-ada-002"
    ) -> List[float]:
        """
        Generate embeddings using LiteLLM
        
        Args:
            text: Text to embed
            model: Embedding model name
            
        Returns:
            List of embedding values
        """
        try:
            response = litellm.embedding(
                model=model,
                input=text
            )
            
            return response.data[0].embedding
        except Exception as e:
            raise Exception(f"Embedding generation failed: {str(e)}")
    
    def get_available_models(self) -> List[str]:
        """
        Get list of available models
        
        Returns:
            List of model names
        """
        return [
            "gpt-3.5-turbo",
            "gpt-4",
            "gpt-4-turbo",
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307",
            "claude-3-opus-20240229"
        ]

# Global AI client instance
ai_client = AIClient()