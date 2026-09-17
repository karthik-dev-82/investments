# Configuration file for the Sphinx documentation builder.

project = "NIFTY Index Terminal — Notes"
copyright = "2026"
author = "Karthik"

extensions = []
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_title = "NIFTY Index Terminal — Notes"

html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 3,
    "titles_only": False,
}
