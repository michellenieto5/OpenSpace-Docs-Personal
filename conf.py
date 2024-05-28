import os

# Generate the files that dynamically depend on asset files in the main OpenSpace repo
with open("generatedocs.py", encoding="utf8") as file:
  try:
    exec(file.read())
  except Exception as e:
    print(e)

###
# Global Settings
###
needs_sphinx = "4.0"

project = "OpenSpace"
author = "OpenSpace community"
project_copyright = "2014-2024, OpenSpace community"

# Update with every new release
version = release = os.getenv("READTHEDOCS_VERSION", "0.20.0")

extensions = [
  "myst_parser",
  "notfound.extension",
  "sphinx_copybutton",
  "sphinx_design",
  "sphinx.ext.autosectionlabel",
  "sphinx.ext.duration",
  "sphinxcontrib.jquery",
  "sphinxcontrib.luadomain",
  "sphinxcontrib.mermaid"
]

keep_warnings = True



###
# Content
###
source_encoding = "utf-8-sig"
exclude_patterns = [
  "README.md",
  ".venv"
]
root_doc = "index"
primary_domain = "lua"
autosectionlabel_prefix_document = True
pygments_style = "default"
pygments_dark_style = "monokai"

myst_enable_extensions = {
  "attrs_inline",
  "colon_fence",
  "fieldlist"
}
myst_heading_anchors = 3



###
# HTML output
###
html_theme = "sphinx_rtd_theme"
html_theme_options = {
  "logo_only" : True,
  "display_version": False,
  "collapse_navigation": False,
}

html_context = {
  "display_github": True,  # Integrate GitHub
  "github_user": "OpenSpace",  # Username
  "github_repo": "OpenSpace-Docs",  # Repo name
}

# Add a transparent image as the logo
# Instead we add the logo later in the css
# This enables different logos in dark and light mode
html_logo = "_static/transparent.png"

html_title = f'OpenSpace documentation ({version})'
html_short_title = "OpenSpace"

html_favicon = "_static/icon.png"

# JavaScript files that are added into the generated documentation
html_js_files = [
  "custom.js"
]

# CSS files that are added into the generated documentation
html_css_files = [
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",

  "required-reading.css",
  "sidebar.css"
]

# These folders are copied to the documentation's HTML output
html_static_path = [ "_static" ]

templates_path = [ "_templates" ]

# html_extra_path = ["robots.txt"]
