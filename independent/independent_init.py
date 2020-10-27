import os
import sys
import django

def django_init():
    # /mqmmw
    PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(PROJECT_DIR)
    # /mqmmw/apps
    BASE_DIR = os.path.join( os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'apps')
    sys.path.append(BASE_DIR)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apps.settings")
    django.setup(set_prefix=False)