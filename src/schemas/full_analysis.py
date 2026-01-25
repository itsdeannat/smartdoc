from pydantic import BaseModel
from schemas.issue import Issue
from schemas.metadata import MetadataSchema
from schemas.metrics import Metrics

class FullAnalysisSchema(BaseModel):
    """Schema for full analysis response from LLM."""
    
    metadata: MetadataSchema
    operations: Metrics
    parameters: Metrics
    schemas: Metrics
    responses: Metrics
    request_bodies: Metrics
    issues: list[Issue]
    recommendations: str