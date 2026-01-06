import os
from dotenv import load_dotenv
import yaml
from openai import OpenAI
from schemas.full_analysis_schema import FullAnalysisSchema

load_dotenv(dotenv_path=".env")

def analyze_full_spec(content: dict):
    """Sends the OpenAPI Specification content to the LLM for analysis.

    Args:
        content (dict): The OpenAPI Specification content as a dictionary.
    """
        
    client = OpenAI()
    
    serialized_oas = yaml.dump(content, sort_keys=False)

    response = client.responses.parse(
        model="gpt-5-mini",
        reasoning={"effort": "low"},
        instructions="You are an OpenAPI specification (OAS) editor with deep knowledge of OpenAPI conventions and best practices. You will be given an OAS file and should analyze it using the given structure. Be concise. Optimize for scanability over completeness. Use a scale of 0-100 for scores. You must report issues as concise diagnostics, not explanations. Issues should read like linter findings. Do not explain best practices or justify why the issue is important. List issues as concise, one-line diagnostics. Prefer fragments over full explanatory sentences.",
        input=serialized_oas,
        text_format=FullAnalysisSchema
    )
    analysis = response.output_parsed
    return analysis

def analyze_descriptions(content: dict):
    """Analyzes only the descriptions in the OpenAPI Specification content.

    Args:
        content (dict): The OpenAPI Specification content as a dictionary.
    """
    client = OpenAI()
    
    serialized_oas = yaml.dump(content, sort_keys=False)

    response = client.responses.parse(
        model="gpt-5-mini",
        reasoning={"effort": "low"},
        instructions="You are an OpenAPI specification (OAS) editor with deep knowledge of OpenAPI conventions and best practices. You will be given an OAS file and should analyze it using the given structure. You must only focus on the descriptions. Be concise. Optimize for scanability over completeness. Use a scale of 0-100 for scores. You must report issues as concise diagnostics, not explanations. Issues should read like linter findings. Do not explain best practices or justify why the issue is important. List issues as concise, one-line diagnostics. Prefer fragments over full explanatory sentences.",
        input=serialized_oas,
        text_format=FullAnalysisSchema
    )
    analysis = response.output_parsed
    return analysis

def display_analysis(analysis: FullAnalysisSchema, focus: str):
    """
    Displays the analysis results in a readable format.
    """
    print("-"*25)
    print("OAS Analysis Results:")
    print("-"*25)
    
    if analysis.issues == []:
        print("No issues found in the OAS file!")
    else:
        for issue in analysis.issues:
            print(f"- {issue.summary}: {issue.message}")

    print("-"*25)
    print("Scores: ")           
    print("-"*25)
    if focus == "descriptions":
        print(f"{'Descriptions':<20}: {analysis.description_coverage}/100")
        print(f"{'Description Clarity':<20}: {analysis.description_clarity}/100")
    # Eventually add other focus areas here
    else:
        print(f"{'Descriptions':<20}: {analysis.description_coverage}/100")
        print(f"{'Description Clarity':<20}: {analysis.description_clarity}/100")
        print(f"{'Naming Consistency':<20}: {analysis.naming_consistency}/100")
        print(f"{'Example Adequacy':<20}: {analysis.example_adequacy}/100")
        print(f"{'Overall Score':<20}: {analysis.overall_score}/100")
