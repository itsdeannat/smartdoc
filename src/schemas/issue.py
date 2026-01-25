from pydantic import BaseModel

class Issue(BaseModel):
    """Schema for individual issues found in the analysis."""
    
    path: str
    issue: str
    action: str