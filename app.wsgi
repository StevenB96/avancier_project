import os
import sys

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the current directory and the virtual environment to the Python path
sys.path.append(current_dir)
venv_path = os.path.join(current_dir, 'venv', 'lib', 'python3', 'site-packages')
sys.path.append(venv_path)

# Load the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
