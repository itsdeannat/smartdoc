from typing_extensions import Annotated
import typer
import os
import analysis_engine.llm_client as llm_client
import oas.yaml_loader as yaml_loader


def find_file(path: str):
    
    if not os.path.isfile(path):
        typer.echo(f"Error: The file '{path}' does not exist.")
        raise typer.Exit(code=1)
    else:
        print(f"File '{path}' found.")

def check(file: Annotated[str, typer.Argument(help="Path to the OpenAPI Specification file to be checked")]):
    """
    Analyzes an OAS file for documentation quality issues using an LLM.
    """ 
    find_file(file)
    content = yaml_loader.load_file(file)
        
    llm_client.analyze_spec(content)
    
    