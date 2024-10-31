# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

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
# html_theme = 'press'
extensions.append("sphinx_wagtail_theme")   # 将主题包含在要加载的扩展列表中, 也就是上面的 extensions 列表中
html_theme = 'sphinx_wagtail_theme'


import os
import sys

# 获取项目根目录路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
print(project_root)

# 将项目根目录路径添加到系统路径中
sys.path.insert(0, project_root)


# These are options specifically for the Wagtail Theme.
html_theme_options = dict(
    project_name = "先智预测",
    # logo = "img/wagtail-logo-circle.svg",
    # logo_alt = "Wagtail",
    logo = r'{}/docs/static/test.svg'.format(project_root),  # 注意路径
    logo_alt = '先智预测_logo',
    logo_height = 59,
    logo_url = "/",
    logo_width = 45,
)



# -- Options for EPUB output
epub_show_urls = 'footnote'
