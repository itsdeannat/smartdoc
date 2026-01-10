from pydantic import BaseModel
from schemas.issue_schema import Issue

class ExamplesAnalysisSchema(BaseModel):
    """Schema for examples analysis response from LLM."""
    
    issues: list[Issue]
    example_adequacy: int
    recommendations: str
    overall_quality: int
    