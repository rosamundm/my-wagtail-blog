from __future__ import absolute_import, unicode_literals
import os
#new for heroku:
from my-wagtail-blog.settings.dev import *

import dj_database_url



from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
