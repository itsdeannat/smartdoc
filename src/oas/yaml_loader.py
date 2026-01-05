import yaml

# Load and parse a sample OpenAPI Specification (OAS) YAML file
def load_file (path: str) -> dict:
    """Loads the OAS YAML file.

    Args:
        path (str): The path to the OAS YAML file.

    Returns:
        dict: The parsed OAS content as a dictionary.
    """
    with open(path) as file:
        yaml_content = yaml.safe_load(file)
    return yaml_content