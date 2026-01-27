=====================
CLI command reference
=====================

You must have SmartDoc CLI installed in your system to access the SmartDoc commands. See the :doc:`Installation topic <installation>` for installation instructions.

Commands
--------

.. list-table::
  :widths: 15 50 
  :align: left
  :header-rows: 1
  
  * - Command syntax
    - Usage

  * - ``analyze [file]``
    - Analyze an OpenAPI Specification (OAS) file for quality and completeness. 

  * - ``summarize [file]``
    - Generate a summary of the API's functionality.

Options
-------

The following options apply to the ``analyze`` command only.

.. list-table::
  :widths: 20 50 
  :align: left
  :header-rows: 1

  * - Command syntax
    - Usage

  * - ``--focus <metric>``
    - Restricts the analysis to a specific metric.

  * - ``--fail-on CATEGORY.METRIC=THRESHOLD``
    - Causes the command to exit with a non-zero status code when the specified condition is met. **Only used with a full analysis**.

