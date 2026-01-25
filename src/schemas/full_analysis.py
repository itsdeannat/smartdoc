from pydantic import BaseModel
from schemas.issue import Issue
from schemas.recommendation import Recommendation
from schemas.metadata import MetadataSchema
from schemas.metric import Metric

class FullAnalysisSchema(BaseModel):
    """Schema for full analysis response from LLM."""
    
    metadata: MetadataSchema
    metrics: list[Metric]
    issues: list[Issue]
    recommendations: list[Recommendation]