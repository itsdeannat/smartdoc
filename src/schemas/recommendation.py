from pydantic import BaseModel

class RecommendationSchema(BaseModel):
    """Schema for recommendations response from LLM."""
    
    summary: str