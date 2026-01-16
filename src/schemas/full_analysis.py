from pydantic import BaseModel
from schemas.issue_schema import Issue
from schemas.recommendation_schema import Recommendation
from schemas.metadata import MetadataSchema

class FullAnalysisSchema(BaseModel):
    """Schema for full analysis response from LLM."""
    
    metadata: MetadataSchema
    issues: list[Issue]
    description_coverage: int
    description_clarity: int
    naming_consistency: int
    example_adequacy: int
    overall_quality: int
    recommendations: list[Recommendation]