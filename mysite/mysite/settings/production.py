from __future__ import absolute_import, unicode_literals

import os

env = os.environ.copy()
SECRET KEY = env['SECRET_KEY']

from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
