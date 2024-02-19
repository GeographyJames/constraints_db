# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import pathlib
import sys
import os


path1 = str(pathlib.Path(__file__).parents[2].resolve().as_posix() / pathlib.Path("src"))
#print("path1 :", path1)
#print(path.is_dir())
#sys.path.insert(0, path)
#path2 = os.path.abspath(os.path.join('..', '..', 'src'))
#print("path2 :", path2)
sys.path.insert(0, path1)
#sys.path.insert(0, path2)
#assert sys.path[0] == sys.path[1]
print(sys.path)


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Constraints Database'
copyright = '2024, James Campbell'
author = 'James Campbell'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
#html_static_path = ['_static']
