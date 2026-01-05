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
    
    # print("API key loaded:", bool(os.getenv("OPENAI_API_KEY")))
    
    
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
    print(f"{'Descriptions':<20}: {analysis.description_coverage}/100")
    print(f"{'Description Clarity':<20}: {analysis.description_clarity}/100")
    print(f"{'Naming Consistency':<20}: {analysis.naming_consistency}/100")
    print(f"{'Example Adequacy':<20}: {analysis.example_adequacy}/100")
    print(f"{'Overall Score':<20}: {analysis.overall_score}/100")
    
    
    
def analyze_descriptions(content: dict):
    """Analyzes only the descriptions in the OpenAPI Specification content.

    Args:
        content (dict): The OpenAPI Specification content as a dictionary.
    """
    
    print("API key loaded:", bool(os.getenv("OPENAI_API_KEY")))
    print("Performing OAS analysis.")
    
    client = OpenAI()
    
    serialized_oas = yaml.dump(content, sort_keys=False)

    response = client.responses.create(
        model="gpt-5-mini",
        reasoning={"effort": "low"},
        instructions="You are an OAS quality assurance specialist. When given an OpenAPI Specification (OAS) document, your task is to evaluate the operation and field descriptions for clarity and completeness. After your analysis, provide a brief summary of the current state of the OAS file. For example, note how many descriptions are missing or vague. After you finish your analysis, use the following metrics to provide a quality score. 1) Description coverage: how many descriptions are present versus missing. 2) Description clarity: how clear and informative the descriptions are. Based on these metrics, assign a grade where 100% indicates complete OAS coverage. Provide specific recommendations for improvement in areas where the OAS falls short. Summarize your findings in a concise report.",
        input=serialized_oas
    )
    print(response.output_parsed)