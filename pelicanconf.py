#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Greg Reinbach'
SITENAME = u'Reinbach'
SITEURL = 'http://www.reinbach.com'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

THEME = 'grandfather'
TEMPLATE_PAGES = {
    'about.html': 'about.html',
}

GOOGLE_ANALYTICS = 'UA-16428972-2'

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/reinbach'),
    ('Twitter', 'https://twitter.com/#!/airggie'),
    ('LinkedIn', 'http://www.linkedin.com/in/reinbach'),
)

DEFAULT_PAGINATION = 5
