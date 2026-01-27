import yaml
import json
from pathlib import Path

# Load and parse a sample OpenAPI Specification (OAS) YAML file
def load_file (path: str) -> dict:
    """Loads the OAS file.

    Args:
        path (str): The path to the OAS YAML or JSON file.

    Returns:
        dict: The parsed OAS content as a dictionary.
    """
    path = Path(path)
    with open(path, "r", encoding="utf-8") as file:
        if path.suffix == ".json":
                return json.load(file)

        if path.suffix in {".yml", ".yaml"}:
            return yaml.safe_load(file)

        raise ValueError(f"Unsupported OAS file type: {path.suffix}")