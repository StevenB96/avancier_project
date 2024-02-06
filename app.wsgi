import os
import sys

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Add the current directory and the virtual environment to the Python path
sys.path.insert(0, current_dir)
sys.path.insert(0, os.path.join(current_dir, 'venv', 'lib', 'python3.11', 'site-packages'))  # Adjust the path and Python version as needed

# Load the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
