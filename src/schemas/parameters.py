from pydantic import BaseModel
from schemas.issue import Issue
from schemas.metadata import MetadataSchema
from schemas.metrics import Metrics

class ParameterSchema(BaseModel):
    """Schema for parameters analysis from LLM."""
    
    metadata: MetadataSchema
    parameters: Metrics
    issues: list[Issue]
    recommendations: str