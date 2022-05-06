import os

if not (os.environ.get('DJANGO_SETTINGS_MODULE') or '').endswith('settings.test'):
    from .base import *  # noqa