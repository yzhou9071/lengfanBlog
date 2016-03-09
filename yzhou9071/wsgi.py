import os
from os.path import join,dirname,abspath

PROJECT_DIR = dirname(dirname(abspath(__file__)))
import sys
sys.path.insert(0,PROJECT_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yzhou9071.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
