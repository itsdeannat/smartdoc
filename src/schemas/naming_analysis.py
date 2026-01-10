from pydantic import BaseModel
from schemas.issue_schema import Issue
from schemas.recommendation_schema import Recommendation

class NamingAnalysisSchema(BaseModel):
    """Schema for naming analysis response from LLM."""
    
    issues: list[Issue]
    naming_consistency: int
    overall_quality: int
    recommendations: list[Recommendation]