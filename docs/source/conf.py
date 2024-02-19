# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import pathlib
import sys
import os


path = str(pathlib.Path(__file__).parents[2].resolve().as_posix() / pathlib.Path("src"))
sys.path.insert(0, path)


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Constraints Database'
copyright = '2024, James Campbell'
author = 'James Campbell'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.intersphinx']


# Mappings to other python module documentation.
intersphinx_mapping = {'sqlalchemy': ('https://docs.sqlalchemy.org/en/20/', None)}

templates_path = ['_templates']
exclude_patterns = []

#suppress_warnings = ['ref.ref'] # This will suppress warnings for all missing ref


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

nitpicky = False
html_theme = 'furo'
#html_static_path = ['_static']
nitpick_ignore = [("doc", "usages"),("ref", "orm_declarative_metadata")] # Only works if nitpicky set to True.