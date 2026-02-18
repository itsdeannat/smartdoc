=====================
Analyzing an OAS file
=====================

The ``analyze`` command allows you to analyze an OpenAPI Specification (OAS) file for quality and completeness. It has one required argument, ``[file]``:

.. code-block:: bash

    smartdoc analyze sample_oas.json

The CLI outputs a message once it starts the analysis. Depending on the size of the OAS file, the analysis may take 10-15 seconds.

Output
------

SmartDoc returns structured JSON output that includes:

1. Analysis metadata
2. The metrics analyzed
3. A list of issues
4. A recommendation for improvement 

Metadata
********

SmartDoc returns metadata about the version, OpenAI model, and date to make executions traceable and easier to debug.

.. code-block:: bash

    "metadata": {
            "smartdoc_version": "0.4.0",
            "openai_model": "gpt-5-mini",
            "analysis_date": "2026-01-25T14:47:59.567990"
        },

Metrics 
*******

SmartDoc reports on metrics for operations, parameters, schemas, responses, and request bodies. For more information about metrics and categories, see the the :doc:`Categories and metrics topic <categories_and_metrics>`.

.. code-block:: bash
    :class: wrap-code

    "operations": {
        "total": 3,
        "missing_descriptions": 2,
        "missing_fields": 3
    },
    "parameters": {
        "total": 2,
        "missing_descriptions": 1,
        "missing_fields": 0
    },
    "schemas": {
        "total": 4,
        "missing_descriptions": 4,
        "missing_fields": 0
    },
    "responses": {
        "total": 6,
        "missing_descriptions": 1,
        "missing_fields": 0
    },
    "request_bodies": {
        "total": 1,
        "missing_descriptions": 1,
        "missing_fields": 0
    },

Issues
******

SmartDoc returns a list of 5-8 findings in its analysis. Each finding contains the associated path, a short summary of the issue, and suggested action to align the file with OAS best practices. 

.. code-block:: bash
    :class: wrap-code

    "issues": [
        {
        "path": "POST /orders operation description",
        "issue": "The operation description is an empty string.",
        "action": "Provide a clear, non-empty description summarizing what this operation does."
        },
        {
        "path": "POST /orders requestBody",
        "issue": "The requestBody has no description property.",
        "action": "Add a concise description to the requestBody explaining the expected payload and any important constraints."
        },
    ]

Recommendations
***************

SmartDoc returns a summary of recommendations actions to improve the OAS file.

.. code-block:: bash
    :class: wrap-code

    "recommendations": "Add meaningful descriptions for every operation, parameter, request body, response, and schema property. Consider adding operationId values and short schema summaries to improve discoverability and client generation."
