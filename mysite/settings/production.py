from __future__ import absolute_import, unicode_literals

import os

SECRET_KEY=os.environ.get('MY_SECRET_KEY_VAR')




from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
