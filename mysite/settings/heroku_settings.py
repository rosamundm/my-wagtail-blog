#production settings for heroku deployment

from my-wagtail-blog.settings.dev import *
from my-wagtail-blog.settings.base import *
from my-wagtail-blog.settings.production import *

import dj_database_url

DATBASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

DEBUG = False

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
