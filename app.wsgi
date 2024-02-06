import os
from django.core.wsgi import get_wsgi_application

# Set the Django settings module environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')

# Load the WSGI application
application = get_wsgi_application()
