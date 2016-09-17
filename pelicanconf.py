#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kyle Willett'
#SITEURL = 'willettk.github.io/blog'
SITENAME = u'Kyle Willett - Blog'

SITETITLE = 'Kyle Willett'
SITESUBTITLE = 'Data Scientist'
SITEDESCRIPTION = 'Projects and Diversions of Kyle Willett'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('main homepage', 'https://willettk.github.io'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/kwwillett'),
          ('github', 'http://github.com/willettk'),
          ('linkedin', 'https://www.linkedin.com/in/willettk'))

TWITTER_USERNAME = 'kwwillett'

DEFAULT_PAGINATION = False

# Theme
THEME = "./Flex"

STATIC_PATHS = [
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2016

MAIN_MENU = True

# Translate to German.
DEFAULT_LANG = 'en'

# Default theme language.
I18N_TEMPLATES_LANG = 'en'

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DATE_FORMATS = {
    'en': '%d %b %Y',
}
