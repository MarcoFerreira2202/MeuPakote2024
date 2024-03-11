import pymysql
pymysql.install_as_MySQLdb()



"""
WSGI config for meu_pacote_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meu_pacote_project.settings')

application = get_wsgi_application()
