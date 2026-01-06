from pydantic import BaseModel

class Issue(BaseModel):
    """Schema for individual issues found in the analysis."""
    
    summary: str
    message: str

class FullAnalysisSchema(BaseModel):
    """Schema for full analysis response from LLM."""
    
    issues: list[Issue]
    description_coverage: int
    description_clarity: int
    naming_consistency: int
    example_adequacy: int
    overall_score: int
    recommendations: str