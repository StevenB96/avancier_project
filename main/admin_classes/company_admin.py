from django.contrib import admin
from .base_admin import BaseAdmin

from ..model_classes import (
    Company,
)


class CompanyAdmin(BaseAdmin):
    exclude = ['id', 'created_at', 'updated_at']


admin.site.register(Company, CompanyAdmin)
