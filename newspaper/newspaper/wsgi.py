"""
WSGI config for newspaper project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

print("Executing \"wsgi.py\"")
import os
print("after import os")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newspaper.settings")
print("after os.env.setdef(\"DJA_SETT_MOD\",\"newsp.sett\")")

# there is a problem inside of here it seems
from django.core.wsgi import get_wsgi_application
print("after from django.core.wsgi import get_w_app")
application = get_wsgi_application()
print("after application = g_w_app()")
