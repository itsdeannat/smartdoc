import yaml
from openai import OpenAI

# Load and parse a sample OpenAPI Specification (OAS) YAML file
def load_file (path: str) -> dict:
    with open(path) as file:
        yaml_content = yaml.safe_load(file)
    print("OAS document loaded successfully.")
    return yaml_content