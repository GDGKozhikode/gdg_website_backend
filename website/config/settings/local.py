"""
Local settings for website project.

- Run in Debug mode

- Use console backend for emails

- Add Django Debug Toolbar
- Add django-extensions as app
"""
from .base import *

# DEBUG
# ----------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# ----------------------------------------------------------------------------
# Note: This key only used for development and testing.
SECRET_KEY = env(
    'SECRET_KEY', default='aJJDEhHqLdlPijfXLStVvnCznQQH2D2xTQkbdf1Qau0Mh2e3I8')

# Mail settings
# ----------------------------------------------------------------------------

EMAIL_PORT = 1025

EMAIL_HOST = 'localhost'
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')

# django-debug-toolbar
# ----------------------------------------------------------------------------
# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
# THIRD_PARTY_APPS += ['debug_toolbar', ]

# INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]

# DEBUG_TOOLBAR_CONFIG = {
#     'DISABLE_PANELS': [
#         'debug_toolbar.panels.redirects.RedirectsPanel',
#     ],
#     'SHOW_TEMPLATE_CONTEXT': True,
# }

# django-extensions
# ----------------------------------------------------------------------------
INSTALLED_APPS += ['django_extensions', ]
