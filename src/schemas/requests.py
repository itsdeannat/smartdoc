from pydantic import BaseModel
from schemas.issue import Issue
from schemas.metadata import MetadataSchema
from schemas.metrics import Metrics

class RequestSchema(BaseModel):
    """Schema for request analysis from LLM."""
    
    metadata: MetadataSchema
    request_bodies: Metrics
    issues: list[Issue]
    recommendations: str