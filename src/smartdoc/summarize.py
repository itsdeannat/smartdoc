from typing_extensions import Annotated
import typer
import os
import analysis_engine.llm_client as llm_client
import oas.yaml_loader as yaml_loader

def summarize(file: Annotated[str, typer.Argument(help="Path to the OpenAPI Specification file to be checked")]):
    """
    Generates a summary of the API's functionality, including available endpoints and HTTP methods.
    """
    content = yaml_loader.load_file(file)
    summary = llm_client.summarize(content)
    print(summary)