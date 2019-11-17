from __future__ import absolute_import, unicode_literals

import os



from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
