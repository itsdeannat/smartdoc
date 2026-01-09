import os
from urllib import response
from dotenv import load_dotenv
import yaml
from openai import OpenAI
from schemas.full_analysis_schema import FullAnalysisSchema

load_dotenv() 

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
        instructions="You are an OpenAPI specification (OAS) editor with deep knowledge of OpenAPI conventions and best practices. You will be given an OAS file and must analyze it using the given structure. For each metric, assign a numeric score between 0 and 100, where higher scores indicate stronger documentation quality for that metric. Report 5-8 findings. Merge related problems into a single finding. Do not list multiple findings for the same issue. Each finding must be one sentence. Each finding must reference exactly one concrete OAS location (path, operation, response code, parameter name, or schema path). Do not include more than one example, schema, or path in a single finding. Do not use conjunctions to list multiple instances (avoid “and”, “or”, commas). Use fragments, not full sentences. Do not explain best practices or justify why the issue is important.",
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

    description_response = client.responses.parse(
        model="gpt-5-mini",
        reasoning={"effort": "low"},
        instructions="You are an OpenAPI specification (OAS) editor with deep knowledge of OpenAPI conventions and best practices. You will be given an OAS file and should analyze it using the given structure. You must only focus on the descriptions. Be concise. Optimize for scanability over completeness. Use a scale of 0-100 for scores. You must report issues as concise diagnostics, not explanations. Issues should read like linter findings. Do not explain best practices or justify why the issue is important. List issues as concise, one-line diagnostics. Prefer fragments over full explanatory sentences.",
        input=serialized_oas,
        text_format=FullAnalysisSchema
    )
    description_response = description_response.output_parsed
    return description_response

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

def summarize (content: dict):
    """Generates a summary of the API's functionality, including available endpoints and HTTP methods.

    Args:
        content (dict): The OpenAPI Specification content as a dictionary.
    """
    client = OpenAI()
    
    serialized_oas = yaml.dump(content, sort_keys=False)

    summary_response = client.responses.create(
        model="gpt-5-mini",
        reasoning={"effort": "low"},
        instructions="You are an OpenAPI specification (OAS) editor with deep knowledge of OpenAPI conventions and best practices. You will be given an OAS file and must generate a short summary of the API's functionality, including available endpoints and HTTP methods. Keep the summary concise and focused on key aspects of the API. The persona is a new developer or technical writer who needs to quickly grasp the API's purpose and capabilities. Brevity is essential; avoid unnecessary details.",
        input=serialized_oas
    )
    summary = summary_response.output_text
    return summary