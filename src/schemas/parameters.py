from pydantic import BaseModel
from schemas.issue import Issue
from schemas.recommendation import RecommendationSchema
from schemas.metadata import MetadataSchema

class ParameterSchema(BaseModel):
    """Schema for parameters analysis from LLM."""
    
    metadata: MetadataSchema
    parameters_total: int
    parameters_missing_descriptions: int 
    issues: list[Issue]
    recommendations: list[RecommendationSchema]