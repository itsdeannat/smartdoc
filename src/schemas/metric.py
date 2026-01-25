from pydantic import BaseModel

class Metric(BaseModel):
    """Schema for individual metrics in the analysis."""
    
    operations_total: int
    operations_missing_descriptions: int
    parameters_total: int
    parameters_missing_descriptions: int
    schemas_total: int
    schemas_missing_descriptions: int
    responses_total: int
    responses_missing_descriptions: int
    request_bodies_total: int
    request_bodies_missing_descriptions: int