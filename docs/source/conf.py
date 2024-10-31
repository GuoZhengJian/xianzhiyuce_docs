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


# -----------------------------------------------------------------------
import sys, os
project_name = r'xianzhiyuce_docs'
# 通过检查 sys.modules 字典来判断当前 Python 解释器中是否已经加载了名为 ipykernel 的模块, 如果为 True 则是在 Jupyter Notebook 环境中
if 'ipykernel' in sys.modules: root_path = os.getcwd()          # 获取 Jupyter Notebook 的工作目录
else: root_path = os.path.dirname(os.path.abspath(sys.argv[0])) # 获取 当前脚本 运行的目录
if project_name in root_path: root_path = root_path.rsplit(project_name, maxsplit = 1)[0]+project_name
else: print('warning: 注意: 无法正确的识别项目根目录, 请检查项目名称 project_name 的值是否设置错误!!!')
if root_path not in sys.path: sys.path.append(root_path)
# -----------------------------------------------------------------------


# These are options specifically for the Wagtail Theme.
html_theme_options = dict(
    project_name = "先智预测",
    logo = r"{}\docs\img\test.svg".format(root_path),
    logo_alt = r"{}/docs/img/test.svg".format(root_path),
    logo_height = 59,
    logo_url = "/",
    logo_width = 45,
)


# -- Options for EPUB output
epub_show_urls = 'footnote'
