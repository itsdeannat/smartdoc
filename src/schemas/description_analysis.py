from pydantic import BaseModel
from schemas.issue_schema import Issue
from schemas.recommendation_schema import Recommendation
from schemas.metadata import MetadataSchema

class DescriptionAnalysisSchema(BaseModel):
    """Schema for full description analysis response from LLM."""
    
    metadata: MetadataSchema
    issues: list[Issue]
    recommendations: list[Recommendation]
    description_coverage: int
    description_clarity: int
    overall_quality: int
