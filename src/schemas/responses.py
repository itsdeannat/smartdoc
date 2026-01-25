from pydantic import BaseModel
from schemas.issue import Issue
from schemas.recommendation import RecommendationSchema
from schemas.metadata import MetadataSchema

class ResponseSchema(BaseModel):
    """Schema for response analysis from LLM."""
    
    metadata: MetadataSchema
    responses_total: int
    responses_missing_descriptions: int 
    issues: list[Issue]
    recommendations: list[RecommendationSchema]