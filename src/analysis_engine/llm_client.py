from dotenv import load_dotenv
import yaml
from openai import OpenAI
from schemas import FullAnalysisSchema, DescriptionAnalysisSchema, ExamplesAnalysisSchema, NamingAnalysisSchema

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

def analyze_focus(content: dict, focus: str):
    """Analyzes a specific focus area in the OpenAPI Specification content.

    Args:
        content (dict): The OpenAPI Specification content as a dictionary.
        focus (str): The specific area to focus the analysis on.
    """
    focus_schemas = {
        "descriptions": DescriptionAnalysisSchema,
        "naming": NamingAnalysisSchema,
        "examples": ExamplesAnalysisSchema
    }
    
    if focus not in focus_schemas:
        raise ValueError(f"Unsupported focus area: {focus}")
    
    client = OpenAI()
    serialized_oas = yaml.dump(content, sort_keys=False)
    focus_response = client.responses.parse(
        model="gpt-5-mini",
        reasoning={"effort": "low"},
        instructions=f"You are an OpenAPI specification (OAS) editor with deep knowledge of OpenAPI conventions and best practices. You will be given an OAS file and you must analyze ONLY the following focus area: {focus_schemas[focus]}. Ignore other parts of the specification. Use a scale of 0-100 for the score. You must report issues as concise diagnostics, not explanations. Issues should read like linter findings. Do not explain best practices or justify why the issue is important. List issues as concise, one-line diagnostics. Prefer fragments over full explanatory sentences.",
        input=serialized_oas,
        text_format=focus_schemas[focus]
    )
    focus_response = focus_response.output_parsed
    return focus_response
    

def display_analysis(analysis, focus=None):
    """
    Displays the analysis results in a readable format.
    """

    data = analysis.model_dump()

    print("-" * 27)
    if focus:
        print(f"OAS Analysis Results ({focus.capitalize()})")
    else: 
        print("OAS Analysis Results (Full)")
    print("-" * 27)
    
    print()
    
    quality_label = get_quality_label(data.get("overall_quality", None), data)
    print(f"Overall Quality: {quality_label}")
    
    print()
    
    print("Key Findings:")
    issues = data.get("issues", [])
    if not issues:
        print("No issues found in the OAS file.")
    else:
        for issue in issues:
            print(f"- {issue['summary']}: {issue['message']}")
            
    if "recommendations" in data and data["recommendations"]:
        print()
        print("Recommendations:")
        recommendations = data.get("recommendations", [])
        if not recommendations:
            print("No recommendations available.")
        else:
            for recommendation in recommendations:
                print(f"- {recommendation['summary']}")
    
    
def get_quality_label(quality_score: int, data) -> str:
    """Returns a quality label based on the overall quality score.

    Args:
        quality_score (int): The overall quality score.

    Returns:
        str: The quality label corresponding to the score.
    """
    
    quality_score = data.get("overall_quality", None)
    
    if quality_score <= 65:
        quality_label = "Needs Improvement"
    elif 65 <= quality_score < 75:
        quality_label = "Fair"
    elif 75 <= quality_score < 90:
        quality_label = "Good"
    else:
        quality_label = "Excellent"
    return quality_label


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