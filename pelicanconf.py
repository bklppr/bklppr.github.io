AUTHOR = 'Benjamin Klepper'
SITENAME = 'Data & Tech Notes'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll - remove it if you don't want a blogroll
LINKS = ()

# Social widget - remove it if you don't want social links
SOCIAL = ()

DEFAULT_PAGINATION = False  # Disable pagination since we only want one articles page

THEME = 'pelican-chunk'  # Make sure this theme is installed and properly configured

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Set the paths for static pages and articles
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']

# URL settings for pages and articles
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

# Add custom menu items for the top navigation bar
MENUITEMS = (
    ('About Me', '/about-me.html'),  # Link to the "About Me" page
    ('Articles', '/index.html'),  # Link to the articles page
)

USE_FOLDER_AS_CATEGORY = False  # Disable using folders as categories
DEFAULT_CATEGORY = ''  # Set the default category to an empty string
DISPLAY_CATEGORIES_ON_MENU = False  # Disable categories in the menu
