from pydantic import BaseModel
from schemas.issue_schema import Issue

class DescriptionAnalysisSchema(BaseModel):
    """Schema for full description analysis response from LLM."""
    
    issues: list[Issue]
    description_coverage: int
    description_clarity: int
    overall_quality: int
