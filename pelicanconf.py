#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Gill'
SITENAME = 'Tetrahedrons & Terminals'
SITETITLE = SITENAME
SITEURL = ''
SITESUBTITLE = u'Thoughts on coding and rpgs'
SITEDESCRIPTION = u'%s\'s Thoughts and Writings' % AUTHOR
BROWSER_COLOR = '#5e4d7c'

THEME = 'themes/flex'

PATH = 'content'

TIMEZONE = 'America/Detroit'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FAVICON = '/images/favicon-red.ico'

STATIC_PATHS = ['images', 'pdfs']

# Menu
MAIN_MENU = True
MENUITEMS = (
	    	('Archives', '/archives.html'),
             	('Categories', '/categories.html'),
             	('Tags', '/tags.html'),
	    )

# Blogroll
LINKS = (
            ('Pelican', 'http://getpelican.com/'),
            ('Python.org', 'http://python.org/'),
            ('Jinja2', 'http://jinja.pocoo.org/'),
        )

# Social widget
SOCIAL = (
             ('tumblr', 'https://dwgill.tumblr.com'),
             ('twitter', 'https://twitter.com/danwgill'),
         )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
