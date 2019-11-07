from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
# env variable, see footer
SECRET_KEY = 'removed'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['127.0.0.1', 'rosamund.pythonanywhere.com']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass


#env variable:
import os

try:
    from private_dev import *
except ImportError: print ("Error: make a local version of private_dev from the template")