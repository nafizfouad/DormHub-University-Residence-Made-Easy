
import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'Hall_Management.settings'
sys.path.insert(0, os.path.abspath('..'))
import django
django.setup()


project = 'Hall Management System - Student'
copyright = '2024, Afzal Hossain Babor'
author = 'Afzal Hossain Babor'
release = '3.9.2'
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
