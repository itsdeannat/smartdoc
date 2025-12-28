from typing_extensions import Annotated
import typer
import os.path
import analysis_engine.llm_client as llm_client
import oas.yaml_loader as yaml_loader

def find_file(path: str):
    is_file = os.path.isfile(path)
    if is_file:
        print(f"File found: {path}")
    else:
        print(f"File not found: {path}")



def check(file: Annotated[str, typer.Argument(help="Path to the OpenAPI Specification file to be checked")]):
      
    if not file:
        typer.echo("No file path provided. Please specify the path to the OAS file.")
        raise typer.Exit(code=1)
    else:
        find_file(file)
        content = yaml_loader.load_file(file)
        
    llm_client.analyze_spec(content)
    
    