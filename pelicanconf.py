#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Andy Kee'
SITENAME = u'Andy Kee'
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
THEME = 'themes/pure-single'
COVER_IMG_URL = 'http://www.andykee.com/theme/images/background.jpg'
FAVICON_URL = 'http://www.andykee.com/theme/images/favicon.ico'
TAGLINE = 'random musings'
GOOGLE_ANALYTICS = 'UA-2815076-3'

# Menu
MENUITEMS = [
    ('all', 'archives.html'),
    #('categories', 'categories.html'),
    ('dev', 'category/dev.html'),
    ('eats', 'categories/eats.html'),
    ('outdoors', 'categoty/outdoors.html'),
    ('travel', 'category/travel.html')
]

# Social links
SOCIAL = (
    ('facebook-square', 'http://facebook.com/andrewkee/'),
    ('instagram', 'http://instagram.com/andykee'),
    ('linkedin-square', 'http://linkedin.com/in/andykee/'),
    ('github', 'https://github.com/andykee/'),
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
