.. smartdoc-cli documentation master file, created by
   sphinx-quickstart on Tue Jan  6 20:50:09 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

SmartDoc CLI Documentation
============================================

What is SmartDoc?
-----------------

SmartDoc is a command-line interface (CLI) tool for analyzing OpenAPI Specification (OAS) files. It surfaces missing details, structural issues, and inconsistencies that makes APIs harder to understand and use. SmartDoc helps teams catch documentation issues early in the development process, improving API quality and the developer experience.

Who it's for
************

* **Developers** creating or updating OpenAPI specifications
* **Technical writers** validating API documentation
* **API teams** getting specs ready for release 

Features
********
* **Powered by OpenAI's GPT-5 model for advanced analysis**: SmartDoc leverages the capabilities of OpenAI's GPT-5 model to perform in-depth analysis of OAS files, providing insights that go beyond basic validation.
* **OpenAPI-Native (YAML and JSON)**: SmartDoc supports both YAML and JSON formats for OpenAPI Specification files, making it versatile for different development environments.
* **Automation-Friendly**: Designed to be integrated into CI/CD pipelines, SmartDoc can automatically analyze OAS files during the development process, ensuring continuous quality checks.
* **Context-Aware Analysis**: SmartDoc evaluates the context of the API definitions, helping to identify issues that may not be apparent through simple schema validation.


.. toctree::
   :hidden:

   installation
   smartdoc_workflow
   metrics



