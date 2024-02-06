from django.contrib import admin
from .base_admin import BaseAdmin
from django import forms
from django_select2.forms import Select2Widget

from ..model_classes import (
    Course,
    Address,
    Party,
    Bookinginvoice,
)


class BookinginvoiceAdminForm(forms.ModelForm):
    class Meta:
        model = Bookinginvoice
        fields = '__all__'
        widgets = {
            'party': Select2Widget,
            'address': Select2Widget,
            'course': Select2Widget
        }
        required = {
            'party': False,
            'address': False,
            'course': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['party'].choices = [
            (party.id, str(party)) for party in Party.objects.all()]
        self.fields['address'].choices = [
            (address.id, str(address)) for address in Address.objects.all()]
        self.fields['course'].choices = [
            (course.id, str(course)) for course in Course.objects.all()]

    party = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )
    address = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )
    course = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )


class BookinginvoiceAdmin(BaseAdmin):
    form = BookinginvoiceAdminForm
    exclude = []


admin.site.register(Bookinginvoice, BookinginvoiceAdmin)
