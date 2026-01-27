from pydantic import BaseModel
from schemas.issue import Issue
from schemas.metadata import MetadataSchema
from schemas.metrics import Metrics

class OperationSchema(BaseModel):
    """Schema for schema analysis from LLM."""
    
    metadata: MetadataSchema
    operations: Metrics
    issues: list[Issue]
    recommendations: str
