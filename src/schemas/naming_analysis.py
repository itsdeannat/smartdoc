from pydantic import BaseModel
from schemas.issue_schema import Issue

class NamingAnalysisSchema(BaseModel):
    """Schema for naming analysis response from LLM."""
    
    issues: list[Issue]
    naming_consistency: int
    overall_quality: int
    recommendations: str