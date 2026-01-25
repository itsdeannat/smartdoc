from pydantic import BaseModel
from schemas.issue import Issue
from schemas.recommendation import RecommendationSchema
from schemas.metadata import MetadataSchema

class FullAnalysisSchema(BaseModel):
    """Schema for full analysis response from LLM."""
    
    metadata: MetadataSchema
    operations_total: int
    operations_missing_descriptions: int
    parameters_total: int
    parameters_missing_descriptions: int
    schemas_total: int
    schemas_missing_descriptions: int
    responses_total: int
    responses_missing_descriptions: int
    request_bodies_total: int
    request_bodies_missing_descriptions: int
    issues: list[Issue]
    recommendations: list[RecommendationSchema]