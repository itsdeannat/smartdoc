from pydantic import BaseModel
from schemas.issue import Issue
from schemas.recommendation import RecommendationSchema
from schemas.metadata import MetadataSchema

class OperationSchema(BaseModel):
    """Schema for schema analysis from LLM."""
    
    metadata: MetadataSchema
    operations_total: int
    operations_missing_descriptions: int 
    issues: list[Issue]
    recommendations: list[RecommendationSchema]
