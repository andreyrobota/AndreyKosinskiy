"""
WSGI config for untitled8 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
<<<<<<< HEAD
=======

>>>>>>> fc3e45350bbd6e02ca2d590c10e9ed7582265998
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled8.settings")

application = get_wsgi_application()
<<<<<<< HEAD
application = DjangoWhiteNoise(application)
=======

application = DjangoWhiteNoise(application)
>>>>>>> fc3e45350bbd6e02ca2d590c10e9ed7582265998
