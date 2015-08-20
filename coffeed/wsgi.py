"""
WSGI config for coffeed project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coffeed.settings")
os.environ['AWSAccessKeyId'] = 'AKIAIA6KAOWQKC27TMPA'
os.environ['AWSSecretKey'] = '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'
os.environ['DBNAME'] = 'coffeed'
os.environ['DBUSER'] = 'gwyn'
os.environ['DBPASSWORD'] = 'bruc1e'
from django.core.wsgi import get_wsgi_application
from dj_static import Cling
application = Cling(get_wsgi_application())
