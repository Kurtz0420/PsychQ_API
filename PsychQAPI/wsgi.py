"""
WSGI config for PsychQAPI project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# assuming your django settings file is at '/home/skurtz00420/mysite/mysite/settings.py'
# and your manage.py is is at '/home/skurtz00420/mysite/manage.py'
path = '/home/skurtz00420/mysite'
if path not in sys.path:
   sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()