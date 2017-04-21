#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Gill'
SITENAME = 'Tetrahedrons & Terminals'
SITETITLE = SITENAME
SITEURL = 'http://localhost:8000'
SITESUBTITLE = u'Thoughts on coding and rpgs'
SITEDESCRIPTION = u'%s\'s thoughts and writings on coding & rpgs' % AUTHOR
COPYRIGHT_YEAR = 2017

_color = {
    'green': '#ACC18A',
    'dark_brown': '#333333',
    'light_brown': '#837a75',
    'white': '#ffffff',
    'red': '#DB400C',
}

BROWSER_COLOR = _color['dark_brown']

THEME = 'themes/flex'

PATH = 'content'

TIMEZONE = 'America/Detroit'

DEFAULT_LANG = 'en'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# STATIC_PATHS = ['images', 'pdfs']
STATIC_PATHS = ['images']

# Insure that the CNAME file is toplevel so Github can find it

FAVICON = '/images/favicon.ico'
SITELOGO = '/images/logo.png'

# Menu
MAIN_MENU = True
MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)

# Blogroll
LINKS = (
    # ('Pelican', 'http://getpelican.com/'),
    # ('Python.org', 'http://python.org/'),
    # ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('tumblr', 'https://dwgill.tumblr.com'),
    ('twitter', 'https://twitter.com/danwgill'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
