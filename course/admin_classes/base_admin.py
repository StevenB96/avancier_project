from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
