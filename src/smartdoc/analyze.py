import os
from typing_extensions import Annotated
import typer
import analysis_engine.llm_client as llm_client
import oas.oas_loader as oas_loader
from .serialize import serialize_to_json
from .metadata import initialize_metadata
from .fail_on import evaluate_fail_on_condition



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


def analyze(file: Annotated[str, typer.Argument(help="Path to the OpenAPI Specification file to be checked")], focus: Annotated[str, typer.Option(help="Restricts the analysis to a specific metric")] = "", fail_on: Annotated[list[str], typer.Option("--fail-on", help="Failure criteria")] = None):
    """
    Analyzes an OpenAPI Specification (OAS) file for quality and completeness using an LLM. Users can specify a focus area for the analysis, such as descriptions.
    """
    find_file(file)
    content = oas_loader.load_file(file)
    if focus:
        analysis_result = llm_client.analyze_focus(content, focus) # If focus, analyze the specific area        
    else:
        analysis_result = llm_client.analyze_full_spec(content) # Else analyze the full spec
        
    initialize_metadata(analysis_result) # Set metadata
    
    serialize_to_json(analysis_result) # Serializes and prints JSON
    
    if fail_on:
        if focus:
            raise typer.BadParameter(
                "--fail-on cannot be used with --focus; only full analysis supports fail-on"
            )
        print()
        evaluate_fail_on_condition(analysis_result, fail_on)