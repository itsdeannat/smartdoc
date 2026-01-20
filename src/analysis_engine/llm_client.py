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
        instructions="You are an OpenAPI specification (OAS) editor with deep knowledge of OpenAPI conventions and best practices. Analyze the given OAS file and return 5-8 findings. Each finding should reference exactly one OAS location but translate technical paths into concise, human-readable sentences. Do not list multiple locations in a single finding. Each finding must include a concise, neutral summary of the issue, the exact OAS location where the issue occurs, and action describing how to fix the issue. Use a pleasant, conversational tone and help the user quickly understand the core issues and how to fix them. Use numeric scores between 0 and 100 for each metric. Merge related problems into a single finding. Do not explain best practices or justify why the issue is important. The user's goal is to produce an OAS file that is clear, complete, and easy to understand for both technical and non-technical stakeholders.",
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
        instructions=f"You are an OpenAPI specification (OAS) editor with deep knowledge of OpenAPI conventions and best practices. Analyze the given OAS file and return 5–8 findings limited strictly to the following focus area: {focus_schemas[focus]}. Ignore all other parts of the specification. Each finding must include a concise, neutral summary of the issue, the exact OAS location where the issue occurs, and action describing how to fix the issue. Each finding should reference exactly one OAS location, translating technical paths into concise, human-readable sentences. Do not list multiple locations in a single finding. Merge closely related problems into a single finding. Use a pleasant, conversational tone and help the user quickly understand the core issue and how to fix it. Do not explain best practices or justify why the issue is important. Use numeric scores between 0 and 100 for each metric. The user’s goal is to produce an OAS file that is clear, complete, and easy to understand for both technical and non-technical stakeholders.",
        input=serialized_oas,
        text_format=focus_schemas[focus]
    )
    focus_response = focus_response.output_parsed
    return focus_response
    
    
    
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