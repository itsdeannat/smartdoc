from pydantic import BaseModel

class Issue(BaseModel):
    """Schema for individual issues found in the analysis."""
    
    summary: str
    path: str
    message: str