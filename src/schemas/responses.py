from pydantic import BaseModel
from schemas.issue import Issue
from schemas.metadata import MetadataSchema
from schemas.metrics import Metrics

class ResponseSchema(BaseModel):
    """Schema for response analysis from LLM."""
    
    metadata: MetadataSchema
    responses: Metrics
    issues: list[Issue]
    recommendations: str