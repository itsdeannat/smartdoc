from pydantic import BaseModel
from schemas.issue_schema import Issue

class FullAnalysisSchema(BaseModel):
    """Schema for full analysis response from LLM."""
    
    issues: list[Issue]
    description_coverage: int
    description_clarity: int
    naming_consistency: int
    example_adequacy: int
    overall_quality: int
    recommendations: str