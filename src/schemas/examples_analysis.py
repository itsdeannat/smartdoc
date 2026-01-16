from pydantic import BaseModel
from schemas.issue_schema import Issue
from schemas.recommendation_schema import Recommendation
from schemas.metadata import MetadataSchema

class ExamplesAnalysisSchema(BaseModel):
    """Schema for examples analysis response from LLM."""
    metadata: MetadataSchema
    issues: list[Issue]
    example_adequacy: int
    recommendations: list[Recommendation]
    overall_quality: int
    