import typer
import os.path
import analysis_engine.prompter as prompter
import oas.file_handler as file_handler

def find_file(path: str):
    is_file = os.path.isfile(path)
    if is_file:
        print(f"File found: {path}")
    else:
        print(f"File not found: {path}")



def check(file: str = typer.Argument(...,help="Path to the OpenAPI Specification file to be checked.")
):
        
    if not file:
        typer.echo("No file path provided. Please specify the path to the OAS file.")
        raise typer.Exit(code=1)
    print(f"Checking the OAS file {file} for issues...")
    
    find_file(file)
    content = file_handler.load_file(file)
    prompter.analyze_content(content)
    
    