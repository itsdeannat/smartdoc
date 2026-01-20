
The SmartDoc workflow
=====================

SmartDoc analyzes OpenAPI Specification (OAS) files using OpenAI's GPT-5-mini model to identify missing details, structural issues, and inconsistencies that make APIs harder to understand and use.

It works in three stages:

1. **Data Extraction**: Extracts paths, operations, summaries, descriptions, parameters, responses, and other relevant information from the OAS file.
2. **Contextual Analysis**: Sends the extracted data to the GPT-5-mini model, which acts as an experienced OAS editor and reviews the specification as a whole or within a user-defined scope.
3. **Report Generation**: Returns the results in JSON, highlighting issues found and providing recommendations for improvement.

This approach allows SmartDoc to provide context-aware analysis that goes beyond simple schema validation, helping to surface documentation issues earlier in the development process and improving API quality and the developer experience.