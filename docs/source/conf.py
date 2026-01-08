# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SmartDoc'
copyright = '2026, Deanna Thompson'
author = 'Deanna Thompson'
release = '0.2.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_theme_options = {
    'description': 'CLI tooling for Smart API Documentation',
    "fixed_sidebar": True,
}
html_theme_options = {
    "globaltoc_collapse": False,
}
html_sidebars = {
    '**': [
        'about.html',
        'searchfield.html',
        'navigation.html',
    ]
}