"""
WSGI config for tt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

#!/usr/bin/python
import os
import sys

here = os.path.dirname(__file__)
sys.path.append(os.path.dirname(here))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
