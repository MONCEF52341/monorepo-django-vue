# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys


project = 'Main'
copyright = '2024, Moncef Mostaine'
author = 'Moncef Mostaine'
release = '0.0.1'

sys.path.insert(0, os.path.abspath(".."))
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
]
templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

autodoc_mock_imports = ["django"]

# Configuration de la sortie HTML
html_theme = "alabaster"
html_static_path = ["_static"]