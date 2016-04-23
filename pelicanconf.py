#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from os.path import expanduser

AUTHOR = u'Han'
SITENAME = u'Note Everything'
SITEURL = 'http://localhost:1515'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

home_dir = expanduser('~')
THEME = '{}/pelican-themes/elegant'.format(home_dir)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

STATIC_PATHS = [
    'extra/CNAME',
    'extra/.gitignore',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/.gitignore': {'path': '.gitignore'},
}

RECENT_ARTICLES_COUNT = 20

MD_EXTENSIONS = [
    'markdown.extensions.nl2br',
    'markdown.extensions.fenced_code',
]
