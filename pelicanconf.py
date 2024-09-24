AUTHOR = 'Benjamin Klepper'
SITENAME = 'Data & Tech Notes'
# SITEURL = ''
# SITEURL = 'http://127.0.0.1:8000'  # local development
SITEURL = 'https://bklppr.github.io'

PATH = 'content'

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

DEFAULT_PAGINATION = 10

THEME = 'attila'  # Make sure this theme is installed and properly configured

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

TAGS_URL = 'tags'
CATEGORIES_URL = 'categories'

# Set the paths for static pages and articles
PAGE_PATHS = ['pages']
POSTS_PATHS = ['posts']

# URL settings for pages and articles
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

POST_URL = 'posts/{slug}.html'
POST_SAVE_AS = 'posts/{slug}.html'

# Add custom menu items for the top navigation bar
MENUITEMS = (
    # ('About', '/pages/about.html'),
    ('Posts', '/index.html'),
)

USE_FOLDER_AS_CATEGORY = False  # Disable using folders as categories
DEFAULT_CATEGORY = 'General'  # Set the default category to an empty string
DISPLAY_CATEGORIES_ON_MENU = False  # Disable categories in the menu
