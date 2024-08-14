##################################################################################
# This is a practice project from Biao Yan (Bob Yan), and it's free to be
# downloaded for study and test project.
##################################################################################

"""
WSGI config for woolworths_mock project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'woolworths_mock.settings')

application = get_wsgi_application()
