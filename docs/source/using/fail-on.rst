===========================
Configuring fail conditions
===========================

If you plan to use SmartDoc with Continuous Integration (CI) pipelines, you can use the ``--fail-on`` flag to cause CI/CD to fail if a specific condition is met.

.. admonition:: --fail-on is for full analyses only
    :class: warning

    You can only use ``--fail-on`` if you run a full analysis of an OAS file. If you try to pass ``--fail-on`` with the ``--focus`` option, the CLI will report an error. You will still see the JSON output.

When using the ``--fail-on`` flag, you must pass the condition you want SmartDoc to evaluate. You must use a ``CATEGORY.METRIC=THRESHOLD`` format in the condition:

.. code-block:: bash

    smartdoc analyze sample_oas.json --fail-on schemas.missing_descriptions=2

If the value in the condition is greater than the value in the results, the fail-on is triggered and the CLI exits with a code 1. 

.. code-block:: bash

    # other results
    "schemas": {
        "total": 4,
        "missing_descriptions": 4,
        "missing_fields": 0
    }

    Evaluating fail-on: schemas.missing_descriptions=2
    Fail-on triggered, exiting 1


Example usage in a CI process (GitHub Actions)
----------------------------------------------

Here's a basic GitHub Actions workflow that runs SmartDoc on YAML files when a pull request is opened.

.. code-block:: yaml
    :class: wrap-code

        name: SmartDoc
        run-name: OAS review

        on:
        pull_request:
            paths:
            - "**/*.yaml"
            - "**/*.yml"

        jobs:
        smartdoc:
            runs-on: ubuntu-latest
            steps:
              - uses: actions/checkout@v4
              - uses: actions/setup-python@v5
                with:
                  python-version: "3.11"

              - name: Install SmartDoc
                run: pip install git+https://github.com/itsdeannat/smartdoc.git@release/0.5.0

              - name: Analyze OpenAPI spec
                run: smartdoc analyze schema.yml --fail-on responses.missing_descriptions=2


    