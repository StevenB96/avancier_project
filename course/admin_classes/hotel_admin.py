from django.contrib import admin
from .base_admin import BaseAdmin
from django import forms
from django_select2.forms import Select2Widget

from ..model_classes import (
    Venue,
    Address,
    Hotel,
)


class HotelAdminForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'
        widgets = {
            'venue': Select2Widget,
            'address': Select2Widget,
        }
        required = {
            'venue': False,
            'address': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['venue'].choices = [
            (venue.id, str(venue)) for venue in Venue.objects.all()]
        self.fields['address'].choices = [
            (address.id, str(address)) for address in Address.objects.all()]

    venue = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )
    address = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )


class HotelAdmin(BaseAdmin):
    form = HotelAdminForm
    exclude = []


admin.site.register(Hotel, HotelAdmin)
