from pydantic import BaseModel

class Recommendation(BaseModel):
    """Schema for recommendations response from LLM."""
    
    summary: str