from django.contrib import admin
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
            'party_id': Select2Widget,
            'address_id': Select2Widget,
            'course_id': Select2Widget
        }
        required = {
            'party_id': False,
            'address_id': False,
            'course_id': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['party_id'].choices = [
            (party._id, str(party)) for party in Party.objects.all()]
        self.fields['address_id'].choices = [
            (address._id, str(address)) for address in Address.objects.all()]
        self.fields['course_id'].choices = [
            (course._id, str(course)) for course in Course.objects.all()]

    party_id = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )
    address_id = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )
    course_id = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )


class BookinginvoiceAdmin(admin.ModelAdmin):
    form = BookinginvoiceAdminForm
    exclude = ['_id', 'attendees']


admin.site.register(Bookinginvoice, BookinginvoiceAdmin)
