from pydantic import BaseModel
from schemas.issue import Issue
from schemas.metadata import MetadataSchema

class RequestSchema(BaseModel):
    """Schema for request analysis from LLM."""
    
    metadata: MetadataSchema
    request_bodies_total: int
    request_bodies_missing_descriptions: int 
    requests_missing_fields: int
    issues: list[Issue]
    recommendations: str