from .base import *
import os
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')
# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
DATABASES = {
        'default':dj_database_url.config(default="mysql://uzmduhmy_josue:Admin123321Admin@single-5922.banahosting.com:3306/uzmduhmy_wagtailb2b", conn_max_age=600),
        }

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
# and renames the files with unique names for each version to support long-term caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# try:
#     from .local import *
# except ImportError:
#     pass
