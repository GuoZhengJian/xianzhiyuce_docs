# Configuration file for the Sphinx documentation builder.

# -- Project information

project = '先智预测 - 使用文档'
copyright = '2024, 先智预测'
author = '先智预测'

release = '0.0.1'
version = '0.0.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

# html_theme = 'sphinx_rtd_theme'
# html_theme = 'nature'
html_theme = 'press'

# -- Options for EPUB output
epub_show_urls = 'footnote'


# 配置 press 主题
# 更多配置请前往 https://schettino72.github.io/sphinx_press_site/configuration.html
html_theme_options = {
  "external_links": [
      ("官方网站", "https://www.xianzhiyuce.com/home/"),
  ]
}