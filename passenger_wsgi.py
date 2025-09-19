import os, sys
sys.path.insert(0, '/home/v/valiev3m/sunnatlife/sunnatlife')
sys.path.insert(1, '/home/v/valiev3m/sunnatlife/sunnatlife/venv/lib/python3.12/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()