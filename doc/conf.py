#
# geoh5py documentation build configuration file, created by
# sphinx-quickstart on Tue Sep 16 16:41:10 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# on_rtd is whether we are on readthedocs.org
import os
import subprocess
import sys
# import geoh5io

sys.path.append(os.path.abspath("./_ext"))
sys.path.append(os.path.abspath(".."))

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = "2.2.1"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'numpydoc',
    'sphinx_issues',
]

# Autosummary pages will be generated by sphinx-autogen instead of sphinx-build
autosummary_generate = []

# numpydoc_class_members_toctree = False

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = False
napoleon_use_rtype = True
napoleon_use_keyword = True
napoleon_custom_sections = None
numpydoc_show_class_members = False
numpydoc_class_members_toctree = False


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "geoh5py"

# The short X.Y version.
version = "0.1.0"
# The full version, including alpha/beta/rc tags.
release = "0.1.0"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "AUTHORS.rst", "table_*", "**.ipynb_checkpoints"]

linkcheck_ignore = [
    "https://en.wikipedia.org/wiki/Seismic_source#/media/*",
    "http://www.sgl.com/technicalpapers/EAGEabst-final-TV.pdf",
    "http://geogratis.gc.ca/site/eng/extraction",
    "http://www.ngdc.noaa.gov/*",
    "http://www.eoas.ubc.ca/courses/eosc350/content/*",
    "http://www.eos.ubc.ca/courses/eosc350/content/*",
    "https://vimeo.com/*",
    "https://www.researchgate.net/*",
]
linkcheck_retries = 3
linkcheck_timeout = 2000

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# API doc options
apidoc_module_dir = "../geoh5io"
apidoc_output_dir = "content/api/generated"
apidoc_toc_file = False
apidoc_excluded_paths = []
apidoc_separate_modules = True

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# -- Edit on Github Extension ---------------------------------------------

edit_on_github_project = "mira/geoh5io"
edit_on_github_branch = "master"
edit_on_github_directory = "docs"

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.


on_rtd = os.environ.get("READTHEDOCS", None) == "True"

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme

    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# otherwise, readthedocs.org uses their theme by default, so no need to specify it

# html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {
#   'display_github': 'True',
# }

check_meta = False

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = "gpg.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "geoh5pyDocumentation"

numfig = True
# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        "index",
        "geoh5pyDocumentation.tex",
        "geoh5py Documentation",
        "MiraGeoscience",
        "manual",
    )
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ("index", "geoh5pyDocumentation", "geoh5py Documentation", ["MiraGeoscience"], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "geoh5pyDocumentation",
        "geoh5py Documentation",
        "MiraGeoscience",
        "geoh5py",
        "API for geoh5 database and Geoscience Analyst.",
        "Miscellaneous",
    )
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {"http://docs.python.org/": None}


# -- User Defined Methods ------------------------------------------------
sys.path.append(os.getcwd())

# from _ext import edit_on_github
# from _ext import copyImages, supress_nonlocal_image_warn, make_lectures_page

# copyImages()

# -- Strip all notebooks before


# def nbstripout():
#     # get relevant directories
#     cwd = os.getcwd()

#     # search for images that have been missed
#     for root, dirList, fileList in os.walk(cwd):
#         if 'Workspace' not in root:
#             for filename in fileList:
#                 if 'ipynb' in filename:
#                     os.system('nbstripout ' + os.path.join(root, filename))


# nbstripout()
## Build the API
# dirname, filename = os.path.split(os.path.abspath(__file__))
# subprocess.run(
#     [
#         "sphinx-autogen",
#         "-i",
#         "-t",
#         os.path.sep.join([dirname, "_templates"]),
#         "-o",
#         os.path.sep.join([dirname, "content/api/generated"]),
#         os.path.sep.join([dirname, "content/api/index.rst"]),
#     ]
# )
