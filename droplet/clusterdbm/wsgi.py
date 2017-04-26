"""
WSGI config for clusterdbm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

from django.core.wsgi import get_wsgi_application

sys.path = sys.path + ["/home/dbmart/dbm/clusterdbm"]


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clusterdbm.settings")

application = get_wsgi_application()
