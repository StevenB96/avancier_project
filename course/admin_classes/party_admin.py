from django.contrib import admin

from ..model_classes import (
    Party,
)


class PartyAdmin(admin.ModelAdmin):
    exclude = ['_id', 'bookinginvoices', 'enquiries']


admin.site.register(Party, PartyAdmin)
