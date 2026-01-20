from pydantic import BaseModel
from datetime import datetime

class MetadataSchema(BaseModel):
    """Schema for metadata information."""
    
    smartdoc_version: str 
    openai_model: str 
    analysis_date: datetime = datetime.now()
    