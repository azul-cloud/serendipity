from .base import *


DEBUG = False
TEMPLATE_DEBUG = False

if DEBUG:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# MIDDLEWARE_CLASSES.append(
#     'sslify.middleware.SSLifyMiddleware',
# )


# Allow all host headers
ALLOWED_HOSTS = [
    'blends.herokuapp.com', 
    'www.serendipityartisanblends.com', 
    'serendipityartisanblends.com'
]