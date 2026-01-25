=============================================
Understanding analysis categories and metrics
=============================================

There are five categories SmartDoc reports on:

* Parameters
* Requests
* Responses 
* Operations 
* Schemas

Specifically, SmartDoc analyzes three metrics per category:

* ``total``: the total number of elements in a category
* ``missing_descriptions``: the number of elements missing descriptions
* ``missing_fields``: the number of elements missing required fields

The full analysis returns categories as top-level keys (e.g. ``operations``, ``paramters``) with metrics inside each category:

.. code-block:: bash

    "operations": {
        "total": 3,
        "missing_descriptions": 2,
        "missing_fields": 3
    },

The focused analysis returns metrics only for the requested category, with the category name embedded in each metric:

.. code-block:: bash

    "operations_total": 3,
    "operations_missing_descriptions": 2
    "operations_missing_fields": 1