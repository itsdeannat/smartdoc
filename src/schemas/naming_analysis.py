from pydantic import BaseModel
from schemas.issue_schema import Issue
from schemas.recommendation_schema import Recommendation
from schemas.metadata import MetadataSchema

class NamingAnalysisSchema(BaseModel):
    """Schema for naming analysis response from LLM."""
    
    metadata: MetadataSchema
    issues: list[Issue]
    naming_consistency: int
    overall_quality: int
    recommendations: list[Recommendation]