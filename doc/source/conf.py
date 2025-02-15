# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
import warnings

master_doc = 'index'
add_module_names = False

def setup(app):
    app.add_stylesheet(os.path.join("css","custom.css"))

# -- Project information -----------------------------------------------------

project = 'Covid Visualization'
copyright = '2021, Jihène Belgaied, Zakaria Laabsi, Chloé Serre-Combe, Stephani Ujka'
author = ' Jihène Belgaied, Zakaria Laabsi, Chloé Serre-Combe, Stephani Ujka'

release = '0.0.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Import modules
autodoc_mock_imports = ['pydeck', 'geopandas']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
pygments_style = 'monokai' 

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------

# warnings.filterwarnings("ignore", category=UserWarning,
#                         message='Matplotlib is currently using agg, which is a'
#                                 ' non-GUI backend, so cannot show the figure.')


# examples_dirs = ['../examples',]
# gallery_dirs = ['_auto_scripts']


# image_scrapers = ('matplotlib',)

# from sphinx_gallery.sorting import FileNameSortKey
# sphinx_gallery_conf = {
#      # path to your examples scripts
#     'examples_dirs': examples_dirs,
#      # path where to save gallery generated examples
#     'gallery_dirs': gallery_dirs,
#     # order of the Gallery
#     'line_numbers': False,
#     'image_scrapers': image_scrapers,
#     'show_memory': False,
# }




