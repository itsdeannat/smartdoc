from pydantic import BaseModel

class Metrics(BaseModel):
    total: int
    missing_descriptions: int
    missing_fields: int