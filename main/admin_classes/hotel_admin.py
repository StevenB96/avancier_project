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
            'venues': Select2Widget,
            'address': Select2Widget,
        }
        required = {
            'venues': False,
            'address': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['venues'].choices = [
            (venues.id, str(venues))
            for venues in Venue.objects.all()]
        self.fields['address'].choices = [
            (address.id, str(address))
            for address in Address.objects.all()]


class HotelAdmin(BaseAdmin):
    form = HotelAdminForm
    exclude = ['id', 'created_at', 'updated_at']


admin.site.register(Hotel, HotelAdmin)
