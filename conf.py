# -*- coding: utf-8 -*-
#
# OpenAnalysis documentation build configuration file, created by
# sphinx-quickstart on Wed Jul 19 12:44:16 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

import sys
import os

sys.path.insert(0, os.path.abspath('../Python/'))

extensions = ['nbsphinx',
              'sphinx.ext.autodoc',
              'sphinx.ext.imgmath',
              'sphinx.ext.githubpages'
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'openanalysis'
copyright = u'2017, OpenWeavers'
author = u'OpenWeavers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'0.1'
# The full version, including alpha/beta/rc tags.
release = u'0.1-dev-alpha'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

autodoc_mock_imports = ['matplotlib', 'networkx', 'gi', 'numpy', 'mpl_toolkits']
# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'classic'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_logo = 'res/logo256.png'
html_favicon = 'res/icon.ico'
applehelp_icon = 'res/logo16.png'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'OpenAnalysisdoc'

# -- Options for LaTeX output ---------------------------------------------
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    'fontpkg': r'''\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    'preamble': r"""\usepackage{atbegshi} % http://ctan.org/pkg/atbegshi
\AtBeginDocument{\AtBeginShipoutNext{\AtBeginShipoutDiscard}}
\documentclass{book}
\usepackage[titles]{tocloft}
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
\usepackage[draft]{minted}\fvset{breaklines=true}
\addto\captionsenglish{\renewcommand{\contentsname}{Table of contents}}'
""",

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',

    # Remove blank pages in pdf
    'classoptions': ',openany,oneside',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex'
}

# nbsphinx_execute = 'always'

# nbsphinx_execute_arguments = ['--InlineBackend.figure_formats={"svg", "pdf"}']

# nbsphinx_allow_errors = True

latex_logo = 'res/logo32.png'

latex_show_urls = 'footnote'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'openanalysis.tex', u'openanalysis Documentation',
     u'OpenWeavers', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'openanalysis', u'openanalysis Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'openanalysis', u'openanalysis Documentation',
     author, 'openanalysis', 'One line description of project.',
     'Miscellaneous'),
]
