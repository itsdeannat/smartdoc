from pydantic import BaseModel
from schemas.issue import Issue
from schemas.recommendation import RecommendationSchema
from schemas.metric import Metric
from schemas.metadata import MetadataSchema

class FullAnalysisSchema(BaseModel):
    """Schema for full analysis response from LLM."""
    
    metadata: MetadataSchema
    metrics: list[Metric]
    issues: list[Issue]
    recommendations: list[RecommendationSchema]