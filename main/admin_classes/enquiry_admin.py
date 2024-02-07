from django.contrib import admin
from .base_admin import BaseAdmin

from ..model_classes import (
    Enquiry,
)


class EnquiryAdmin(BaseAdmin):
    exclude = ['id', 'created_at', 'updated_at']


admin.site.register(Enquiry, EnquiryAdmin)
