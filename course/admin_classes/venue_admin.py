from django.contrib import admin
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


class VenueAdmin(admin.ModelAdmin):
    form = VenueAdminForm
    exclude = ['_id', 'courses', 'hotels']


admin.site.register(Venue, VenueAdmin)
