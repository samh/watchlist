"""
WSGI config for django16test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "watchlist.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Serve static files directly
# from dj_static import Cling
# application = Cling(get_wsgi_application())
