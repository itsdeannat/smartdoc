from schemas.metadata import MetadataSchema

def initialize_metadata(analysis):
    """Sets the metadata for the analysis.

    Args:
        analysis: The analysis object to set metadata for.
        smartdoc_version (str): The version of SmartDoc being used.
        openai_model (str): The OpenAI model used for analysis.
    """

    analysis.metadata = MetadataSchema(
        smartdoc_version="0.5.0",
        openai_model="gpt-5-mini",
    )
    