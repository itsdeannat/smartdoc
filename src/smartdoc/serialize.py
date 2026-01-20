import json
from pydantic import BaseModel, Field
   
def serialize_to_json(data: BaseModel):
    """Converts a Pydantic model to JSON for output to stdout

    Args:
        data (BaseModel): The Pydantic model to serialize.

    Returns:
        str: The serialized JSON string.
    """
    json_output = data.model_dump_json(indent=2)
    print(json_output)