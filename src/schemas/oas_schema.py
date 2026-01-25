from pydantic import BaseModel
from schemas.issue import Issue
from schemas.metadata import MetadataSchema

class OASSchema(BaseModel):
    """Schema for schema analysis from LLM."""
    metadata: MetadataSchema
    schemas_total: int
    schemas_missing_descriptions: int 
    schemas_missing_fields: int
    issues: list[Issue]
    recommendations: str
    