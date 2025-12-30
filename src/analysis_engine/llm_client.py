import os
from dotenv import load_dotenv
import yaml
from openai import OpenAI

load_dotenv(dotenv_path=".env")

def analyze_spec(content: dict):
    """Sends the OpenAPI Specification content to the LLM for analysis.

    Args:
        content (dict): The OpenAPI Specification content as a dictionary.
    """
    
    print("API key loaded:", bool(os.getenv("OPENAI_API_KEY")))
    print("Checking the OAS file for issues...")
    
    client = OpenAI()
    
    serialized_oas = yaml.dump(content, sort_keys=False)

    response = client.responses.create(
        model="gpt-5-mini",
        reasoning={"effort": "low"},
        instructions="You are an OAS quality assurance specialist. When given an OpenAPI Specification (OAS) document, your task is to evaluate the following components for clarity and completeness: operation and field descriptions, examples, naming conventions, and overall adherence to OAS best practices. After your analysis, provide a brief summary of the current state of the OAS file. For example, note how many descriptions are missing or vague. After you finish your analysis, use the following metrics to provide a quality score. 1) Description coverage: how many descriptions are present versus missing. 2) Description clarity: how clear and informative the descriptions are. 3) Naming consistency: how well the naming conventions are followed throughout the document. 4) Example adequacy: how well the provided examples illustrate the intended use cases. Based on these metrics, assign a grade where 100% indicates complete OAS coverage. Provide specific recommendations for improvement in areas where the OAS falls short. Summarize your findings in a concise report.",
        input=serialized_oas
    )
    print(response.output_text)