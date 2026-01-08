
The SmartDoc workflow
=====================

SmartDoc analyzes OpenAPI Specification (OAS) files using OpenAI's GPT-5-mini model to identify missing details, structural issues, and inconsistencies that make APIs harder to understand and use.

It works in three stages:

1. **Data Extraction**: Extracts paths, operations, summaries, descriptions, parameters, responses, and other relevant information from the OAS file.
2. **Contextual Analysis**: Sends the extracted data to the GPT-5-mini model, which evaluates the content against multiple quality metrics, such as completeness, clarity, consistency, and adherence to OAS best practices.
3. **Report Generation**: Compiles the results into a structured report, highlighting issues found.

This approach allows SmartDoc to provide context-aware analysis that goes beyond simple schema validation, helping teams catch documentation issues early in the development process.