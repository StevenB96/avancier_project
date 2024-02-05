from django.contrib import admin
from pymongo import MongoClient
from django.conf import settings

default_db_settings = settings.DATABASES['default']
mongo_uri = f"mongodb://{default_db_settings['HOST']}:{default_db_settings['PORT']}/{default_db_settings['NAME']}"

class BaseAdmin(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        client = MongoClient(mongo_uri)
        self.db = client[default_db_settings['NAME']]
