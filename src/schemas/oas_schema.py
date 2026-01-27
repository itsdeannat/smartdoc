from pydantic import BaseModel
from schemas.issue import Issue
from schemas.metadata import MetadataSchema
from schemas.metrics import Metrics

class OASSchema(BaseModel):
    """Schema for schema analysis from LLM."""
    metadata: MetadataSchema
    schemas: Metrics
    issues: list[Issue]
    recommendations: str
    