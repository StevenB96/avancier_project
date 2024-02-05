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
            'address_id': Select2Widget,
        }
        required = {
            'address_id': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['address_id'].choices = [
            (address._id, str(address)) for address in Address.objects.all()]

    address_id = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )


class VenueAdmin(BaseAdmin):
    form = VenueAdminForm
    exclude = ['_id', 'courses', 'hotels']

    def get_search_results(self, request, queryset, search_term):
        addressesList = self.db['address'].find()
        venueList = [address.get('venue')['_id']
                for address in addressesList if address.get('venue')]
        queryset = Venue.objects.filter(_id__in=venueList)

        return queryset, False


admin.site.register(Venue, VenueAdmin)
