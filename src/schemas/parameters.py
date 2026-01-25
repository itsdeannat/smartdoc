from pydantic import BaseModel
from schemas.issue import Issue
from schemas.metadata import MetadataSchema

class ParameterSchema(BaseModel):
    """Schema for parameters analysis from LLM."""
    
    metadata: MetadataSchema
    parameters_total: int
    parameters_missing_descriptions: int 
    parameters_missing_fields: int
    issues: list[Issue]
    recommendations: str