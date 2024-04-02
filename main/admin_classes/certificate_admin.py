from django.contrib import admin
from .base_admin import BaseAdmin

from ..model_classes import (
    Certificate,
)


class CertificateAdmin(BaseAdmin):
    exclude = ['id', 'created_at', 'updated_at']


admin.site.register(Certificate, CertificateAdmin)
