import datetime
from typing_extensions import Annotated
import typer
import os
import analysis_engine.llm_client as llm_client
import oas.yaml_loader as yaml_loader
from schemas.metadata import MetadataSchema
from .serialize import serialize_to_json


def find_file(path: str):
    """Checks if the OAS file exists.

    Args:
        path (str): The path to the OAS YAML file.

    Raises:
        typer.Exit: If the file does not exist.
    """
    
    if not os.path.isfile(path):
        typer.echo(f"Error: The file '{path}' does not exist.")
        raise typer.Exit(code=1)
    else:
        print("Performing OAS analysis.")
        print(f"{path}")


def check(file: Annotated[str, typer.Argument(help="Path to the OpenAPI Specification file to be checked")], focus: Annotated[str, typer.Option(help="Specific area to focus the analysis on")] = "", output: Annotated[str, typer.Option(help="The output method")] = ""):
    """
    Analyzes an OpenAPI Specification (OAS) file for quality and completeness using an LLM. Users can specify a focus area for the analysis, such as descriptions.
    """
    find_file(file)
    content = yaml_loader.load_file(file)
    if focus:
        analysis = llm_client.analyze_focus(content, focus) # If focus, analyze the specific area
        if output == "json": # If users passes json output flag, serialize to json
            analysis.metadata = MetadataSchema(
                smartdoc_version="0.3.0",
                openai_model="gpt-5-mini",
            )
            serialize_to_json(analysis)
    else:
        analysis = llm_client.analyze_full_spec(content)
        if output == "json":
            analysis.metadata = MetadataSchema(
                smartdoc_version="0.3.0",
                openai_model="gpt-5-mini",
            )
            serialize_to_json(analysis)
        else:
            llm_client.display_analysis(analysis)