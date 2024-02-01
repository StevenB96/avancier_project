from django.contrib import admin

from ..model_classes import (
    Address,
)


class AddressAdmin(admin.ModelAdmin):
    exclude = ['_id', 'venue', 'hotel', 'bookinginvoices']


admin.site.register(Address, AddressAdmin)
