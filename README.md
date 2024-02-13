# Django Project Setup README

## Find Installed Versions of Python

To list installed versions of Python and their paths, use the following command:

py -0p --list-paths

## Change Environment Variables to Change Python Version

Adjust environment variables to switch Python versions as needed.

## Initiate a Virtual Environment

Create a virtual environment using the following command:

python -m venv ./venv

## Activate a Virtual Environment

Activate the virtual environment:

venv\Scripts\Activate.ps1

## Setup Django Project

Create a new Django project:

django-admin startproject django_experiment

Create a Django app within the project:

python manage.py startapp polls

## Run Server

Start the Django development server:

python manage.py runserver

## Set execute permission for directories
chmod +x /home/admin/avancier_project/
chmod +x /home/admin/avancier_project/static/

## Set read permission for all files and directories within the Django application directory
chmod -R o+r /home/admin/avancier_project/

## If using SQLite you must do the following
chmod 777 /home/admin/avancier_project
chmod 766 /home/admin/avancier_project/db.sqlite3

## Run Migrations

Apply initial migrations:

python manage.py migrate

## Exit SQLite

To exit the SQLite shell, use:

; + Enter
.quit + Enter

## Make Migrations

Create migrations for a specific app:

python manage.py makemigrations project_1

## Show Migration as SQL Statement

View the SQL statement for a migration:

python manage.py sqlmigrate project_1 0001

## Migrate Everything

Apply all migrations:

python manage.py migrate

## Run Django Shell

Access the Django shell:

python manage.py shell

## Add a Django Admin User

Create a superuser for Django Admin:

python manage.py createsuperuser

Provide the requested information, such as:

- Username: admin
- Email address: admin@example.com
- Password: admin

## Generic Views

Use generic views in Django, for example:

views.IndexView.as_view()
class IndexView(generic.ListView)

## Date Manipulation

Perform date manipulation, for example:

pub_date=timezone.now() + datetime.timedelta(days=30)

## Running Tests

Execute tests for a Django project:

python manage.py test project_1

## Django Test Client (Headless Browser)

Use the Django Test Client:

from django.test.utils import setup_test_environment

## Customize Admin Form

Customize Django Admin forms as needed.

## Customizing Project Templates

To customize project templates, find the Django path:

python -c "import django; print(django.__path__)"

Feel free to adjust the formatting or content as per your needs.