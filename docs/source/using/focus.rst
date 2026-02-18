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

    These are the fundamental building blocks of an API. If these elements are not documented, or are documented incorrectly, developers won't know how to use your API effectively, which can lead to confusion, errors, and wasted time and money. By focusing on these building blocks, SmartDoc ensures the API is usable and predictable.

Example usage
-------------

If you run ``smartdoc analyze sample_oas.json --focus requests``, SmartDoc returns a focused list of metrics and issues.

.. code-block:: bash
    :class: wrap-code

    "operations": {
        "total": 11,
        "missing_descriptions": 11,
        "missing_fields": 1
    },
    "issues": [
        {
        "path": "POST /orders operation description",
        "issue": "Operation has an empty description.",
        "action": "Add a clear, concise description explaining what creating an order does, its important side effects, and any preconditions or expectations for the request body."
        },
        {
        "path": "GET /orders/{orderId} 200 response description",
        "issue": "Successful response (200) has an empty description.",
        "action": "Provide a brief description of the 200 response clarifying what the returned payload represents and any important conditions under which it is returned."
        },
    ]