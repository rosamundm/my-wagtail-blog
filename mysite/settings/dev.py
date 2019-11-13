from .base import *
import os

SECRET_KEY = os.environ.get('SECRET_KEY_VAR')



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['127.0.0.1', 'rosamund.pythonanywhere.com']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
