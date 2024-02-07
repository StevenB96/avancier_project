from django.contrib import admin
from .base_admin import BaseAdmin
from django import forms
from django_select2.forms import Select2Widget

from ..model_classes import (
    Address,
    Venue
)


class VenueAdminForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'
        widgets = {
            'address': Select2Widget,
        }
        required = {
            'address': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['address'].choices = [
            (address.id, str(address)) for address in Address.objects.all()]

    address = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )


class VenueAdmin(BaseAdmin):
    form = VenueAdminForm
    exclude = ['id', 'created_at', 'updated_at']


admin.site.register(Venue, VenueAdmin)
