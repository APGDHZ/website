from __future__ import unicode_literals

AUTHOR = 'The VIANNA research team'
SITENAME = 'VIANNA'
SITEURL = 'http://vianna.de'
CC_LICENSE = 'CC-BY'
AVATAR = 'images/vianna_globe.png'
ABOUT_ME = " "

LINKS = [['Impressum', "/impressum.html"],
         ['MHH Homepage', "http://mh-hannover.de"],
         ['NIFE', "http://nife-hannover.de"],
         ['Hearing4all', "http://hearing4all.eu"]]

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'  # use filesystem date if not given in article
USE_FOLDER_AS_CATEGORY = True

THEME = 'VIANNA-theme'

# Some hand-crafted entries (links) in the main menu
# MENUITEMS = [('foo', 'http://foo.org')]

# Social stuff?
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_CATEGORY = "news"

DISPLAY_CATEGORIES_ON_MENU = True

DISPLAY_TAGS_ON_SIDEBAR = True

DISPLAY_CATEGORIES_ON_SIDEBAR = False

DISPLAY_RECENT_POSTS_ON_SIDEBAR = False

SOCIAL = None

###############################################################################
# Technical stuff ahead. You probably don't need to worry beyond this point.
###############################################################################


OUTPUT_PATH = "../html"  # relative to the pelicanconf.py file


# Always copy these to output, so they get uploaded.
STATIC_PATHS = ['images', '__downloads', 'custom-css/VIANNA.css', '.htaccess']

# The dir to process input files (relative to pelicanconf.py)
PATH = '.'

DEFAULT_PAGINATION = True

# We don't need a page listing the different authors
AUTHORS_SAVE_AS = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True  # Note: gets overwritten in production setup!

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'custom-css/VIANNA.css': {'path': 'static/VIANNA.css'}
}
CUSTOM_CSS = 'static/VIANNA.css'

SITELOGO = 'mhh.png'
SITELOGO_SIZE = '75 em'

FAVICON = "images/favicon.png"  # small icon, shown in adress bar of browsers

# The plugins to load
# Note, `hierarchy` is our own plugin for hierachic static pages.
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['hierarchy']

MD_EXTENSIONS = ['markdown.extensions.extra',
                 'markdown.extensions.sane_lists',
                 'markdown.extensions.toc',
                 'markdown.extensions.headerid',
                 'markdown.extensions.smarty']

# Needed for inclusion of IPython notebooks
# See <https://github.com/getpelican/pelican-plugins/tree/master/liquid_tags>
# if os.path.exists('_nb_header.html'):
#     EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
DISPLAY_BREADCRUMBS = True
# WITH_FUTURE_DATES = False

FILENAME_METADATA = r'(?P<title>((?!-(en|de)).)+)(-(?P<lang>(en|de)))?'
STATIC_LANG_SAVE_AS = "{path}"
