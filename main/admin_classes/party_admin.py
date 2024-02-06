from django.contrib import admin
from .base_admin import BaseAdmin

from ..model_classes import (
    Party,
)


class PartyAdmin(BaseAdmin):
    exclude = []


admin.site.register(Party, PartyAdmin)
