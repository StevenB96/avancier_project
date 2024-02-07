from django.contrib import admin
from .base_admin import BaseAdmin
from django import forms
from django_select2.forms import Select2Widget

from ..model_classes import (
    Attendee,
    Bookinginvoice,
)


class AttendeeAdminForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = '__all__'
        widgets = {
            'bookinginvoices': Select2Widget,
        }
        required = {
            'bookinginvoices': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['bookinginvoices'].choices = [(bookinginvoices.id, str(
            bookinginvoices)) for bookinginvoices in Bookinginvoice.objects.all()]

    bookinginvoices = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )


class AttendeeAdmin(BaseAdmin):
    form = AttendeeAdminForm
    exclude = ['id', 'created_at', 'updated_at']


admin.site.register(Attendee, AttendeeAdmin)
