============
Installation
============

Follow the steps below to install SmartDoc on your system.

.. note::
    SmartDoc is currently source-only. Pre-built packages are coming in a future release.

Prerequisites
-------------

* An OpenAI API key from `OpenAI <https://platform.openai.com/signup>`_
* pip 
* Python 3.10 or later 

Step 1: Clone the source repository
-----------------------------------

.. code-block:: bash

   git clone https://github.com/itsdeannat/smartdoc
   cd smartdoc

Step 2: Create and activate a virtual environment (optional)
----------------------------------------------------------------------------

.. code-block:: bash

   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Step 3: Install the required dependencies
-----------------------------------------

.. code-block:: bash

   pip install -r requirements.txt

Step 4: Add your OpenAI API key
-------------------------------

SmartDoc uses OpenAI's GPT-5-mini model for analysis, so you'll need to set your OpenAI API key as an environment variable. 

After you obtain your API key, add it to a ``.env`` file in your project directory:

.. code-block:: bash

   echo "OPENAI_API_KEY=your_api_key_here" > .env

Replace ``your_api_key_here`` with your actual OpenAI API key.

Step 5: Verify the installation
-------------------------------

To verify that SmartDoc is installed correctly, run the following command:

.. code-block:: bash

    smartdoc --help

You should see the help message for SmartDoc CLI, indicating that the installation was successful.