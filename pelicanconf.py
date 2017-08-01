#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Andy Kee'
SITENAME = 'ANDYKEE'
#SITEURL = 'http://andykee.com'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

TYPOGRIFY = False

DATE_FORMATS = {'en': '%b %d, %Y'}

PLUGIN_PATHS = ['plugins']
MATH_JAX = {'color':'#555'} # https://github.com/barrysteyn/pelican_plugin-render_math

STATIC_PATHS = ['img','pages']

# Theme settings
#THEME = 'themes/tech-engineering'
#PLUGINS = ['render_math', 'tipue_search']
#DIRECT_TEMPLATES = ['index','tags','categories','search']


THEME = 'themes/octavore'
PYGMENTS_THEME = 'solarizeddark'
PLUGINS = ['render_math']
DIRECT_TEMPLATES = ['index','categories']

#FAVICON_URL = 'http://www.andykee.com/theme/images/favicon.ico'
GOOGLE_ANALYTICS = 'UA-2815076-3'

