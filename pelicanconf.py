#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Andy Kee'
SITENAME = 'AK'
#SITEURL = 'http://andykee.com'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

TYPOGRIFY = False

DATE_FORMATS = {'en': '%b %d, %Y'}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math']

STATIC_PATHS = ['img']

# Theme settings
THEME = 'themes/tech-engineering'
FAVICON_URL = 'http://www.andykee.com/theme/images/favicon.ico'
GOOGLE_ANALYTICS = 'UA-2815076-3'

LINKS = (
    ('Facebook', 'http://facebook.com/andrewkee/'),
    ('Instagram', 'http://instagram.com/andykee'),
    ('Linkedin', 'http://linkedin.com/in/andykee/'),
    ('Github', 'https://github.com/andykee/'),
)
# YOUTUBE!
# the first value of the tuple is the icon name from http://fontawesome.io/icons/ after stripping `fa-` (eg. `fa-github` will be `github`)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
