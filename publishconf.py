#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


# Relative URLs break RSS & Atom feeds
RELATIVE_URLS = False


DELETE_OUTPUT_DIRECTORY = True

_use_custom_domain = True
if _use_custom_domain:
    SITEURL = 'http://dwgill.com'
    try:
        STATIC_PATHS += ['extra/CNAME']
    except NameError: # STATIC_PATHS wasn't defined
        STATIC_PATHS = ['extra/CNAME']

    try:
        EXTRA_PATH_METADATA.update({
            'extra/CNAME': {'path': 'CNAME'}
        })
    except NameError: # EXTRA_PATH_METADATA wasn't defined
        EXTRA_PATH_METADATA = {
            'extra/CNAME': {'path': 'CNAME'}
        }
else:
    SITEURL = 'https://dwgill.github.io'


FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

SOCIAL.append(('rss', SITEURL + '/' + FEED_ALL_ATOM))

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
