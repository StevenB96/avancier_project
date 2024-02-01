from django.contrib import admin
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
            'venue_id': Select2Widget,
            'address_id': Select2Widget,
        }
        required = {
            'venue_id': False,
            'address_id': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['venue_id'].choices = [
            (venue._id, str(venue)) for venue in Venue.objects.all()]
        self.fields['address_id'].choices = [
            (address._id, str(address)) for address in Address.objects.all()]

    venue_id = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )
    address_id = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )


class HotelAdmin(admin.ModelAdmin):
    form = HotelAdminForm
    exclude = ['_id']


admin.site.register(Hotel, HotelAdmin)
