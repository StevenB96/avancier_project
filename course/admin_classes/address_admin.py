from django.contrib import admin
from .base_admin import BaseAdmin

from ..model_classes import (
    Address,
)


class AddressAdmin(BaseAdmin):
    exclude = ['_id', 'venue', 'hotel', 'bookinginvoices']


admin.site.register(Address, AddressAdmin)
