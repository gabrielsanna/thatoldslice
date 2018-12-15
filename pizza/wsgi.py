"""
WSGI config for pizza project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizza.settings")

application = get_wsgi_application()

sys.path.append('/var/www/thatoldslice/public_wsgi')
sys.path.append('/var/www/thatoldslice/public_wsgi/pizza')