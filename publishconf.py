#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

_use_dwgill_com = True

RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

if _use_dwgill_com:
    SITEURL = 'http://dwgill.com'
    try:
        STATIC_PATHS += ['extra/CNAME']
    except NameError: # STATIC_PATHS wasn't defined
        STATIC_PATHS = ['extra/CNAME']

    EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
else:
    SITEURL = 'https://dwgill.github.io'


# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
