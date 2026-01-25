from pydantic import BaseModel
from schemas.issue import Issue
from schemas.metric import Metric
from schemas.recommendation import RecommendationSchema
from schemas.metadata import MetadataSchema

class ParameterSchema(BaseModel):
    """Schema for parameters analysis from LLM."""
    
    metadata: MetadataSchema
    metrics: list[Metric]
    issues: list[Issue]
    recommendations: list[RecommendationSchema]