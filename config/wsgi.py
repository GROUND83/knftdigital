"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from django.conf import settings
import config.settings
from django.core.wsgi import get_wsgi_application

# dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# if settings.DEBUG:
#     dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

application = get_wsgi_application()
