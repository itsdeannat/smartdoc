from typing_extensions import Annotated
import typer
import os
import sys
import analysis_engine.llm_client as llm_client
import oas.yaml_loader as yaml_loader
from .serialize import serialize_to_json
from .metadata import initialize_metadata



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


def check(file: Annotated[str, typer.Argument(help="Path to the OpenAPI Specification file to be checked")], focus: Annotated[str, typer.Option(help="Specific area to focus the analysis on")] = "", fail_on: Annotated[str, typer.Option("--fail-on", help="Failure criteria")] = ""):
    """
    Analyzes an OpenAPI Specification (OAS) file for quality and completeness using an LLM. Users can specify a focus area for the analysis, such as descriptions.
    """
    find_file(file)
    content = yaml_loader.load_file(file)
    if focus:
        analysis_result = llm_client.analyze_focus(content, focus) # If focus, analyze the specific area        
    else:
        analysis_result = llm_client.analyze_full_spec(content) # Else analyze the full spec
        
    initialize_metadata(analysis_result) # Set metadata
    
    serialize_to_json(analysis_result) # Serializes and prints JSON
    
    if fail_on:
        print(f"Evaluating fail-on: {fail_on}")
        if ">" in fail_on:
            metric_name, threshold_str = fail_on.split(">")
            threshold = int(threshold_str)
            metric_value = getattr(analysis_result, metric_name, None)
            
            if metric_value is None:
                print(f"Metric '{metric_name}' not found")
            elif metric_value > threshold:
                print("Fail-on triggered, exiting 1")
                sys.exit(1)