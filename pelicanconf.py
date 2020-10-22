#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os

from dotenv import (
    find_dotenv, load_dotenv
)

from pathlib import Path


load_dotenv(find_dotenv())

AUTHOR = 'Matthew Almeida'
SITENAME = 'Matthew Almeida'
SITEURL = ''

PATH = './content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

TYPOGRIFY = True

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GITHUB_URL = 'https://github.com/matthewalmeida'

LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://www.python.org/'),
    ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
)

SOCIAL = (
    ('LinkedIn (MatthewAlmeida)', 'https://www.linkedin.com/in/matthew-almeida/'),
    ('GitHub (MatthewAlmeida)', 'https://www.github.com/MatthewAlmeida'),
    ('Twitter (@Matthew_UMB_ML)', 'https://twitter.com/@Matthew_UMB_ML'),
)

DEFAULT_PAGINATION = 10

THEMES_BASE_DIR = Path(os.getenv("THEMES_BASE_DIR"))
PLUGINS_BASE_DIR = Path(os.getenv("PLUGINS_BASE_DIR"))
THEME_NAME = Path(os.getenv("THEME_NAME"))

THEME = THEMES_BASE_DIR/THEME_NAME
PLUGIN_PATHS = [PLUGINS_BASE_DIR]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
