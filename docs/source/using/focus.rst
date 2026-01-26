=====================
Focusing the analysis
=====================

If you don't want to analyze the entire OAS file, you can specify a specific category for analysis. To focus the analysis, you use the ``--focus`` option. 

The categories for analysis are:

* Parameters
* Requests
* Responses 
* Operations 
* Schemas

.. admonition:: Why these categories?
    :class: note

    These are the fundamental building blocks of an API. If these elements are not documented, or are documented incorrectly, developers won't know how to use your API effectively, which can lead to confusion, errors, and wasted time and money. By focusing on these building blocks, SmartDoc ensures the API is usable, predictable, and easy to integrate.

Example usage
-------------

If you run ``smartdoc analyze sample_oas.json --focus requests``, SmartDoc returns a focused list of metrics and issues.

.. code-block:: bash
    :class: wrap-code

    "request_bodies_total": 1,
    "request_bodies_missing_descriptions": 1,
    "requests_missing_fields": 2,
    "issues": [
        {
        "path": "POST /orders operation description",
        "issue": "The operation description is empty.",
        "action": "Provide a concise, non-empty description for the POST /orders operation that explains what the endpoint does, expected inputs, and any notable behavior."
        },
        {
        "path": "POST /orders requestBody",
        "issue": "The requestBody object has no description.",
        "action": "Add a descriptive requestBody.description that summarizes the structure and purpose of the request payload for this endpoint."
        },
    ]