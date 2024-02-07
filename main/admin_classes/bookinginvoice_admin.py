from django.contrib import admin
from .base_admin import BaseAdmin
from django import forms
from django_select2.forms import Select2Widget

from ..model_classes import (
    Course,
    Contact,
    Bookinginvoice,
)


class BookinginvoiceAdminForm(forms.ModelForm):
    class Meta:
        model = Bookinginvoice
        fields = '__all__'
        widgets = {
            'contacts': Select2Widget,
            'courses': Select2Widget,
        }
        required = {
            'contacts': False,
            'courses': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['contacts'].choices = [
            (contacts.id, str(contacts)) for contacts in Contact.objects.all()]
        self.fields['courses'].choices = [
            (courses.id, str(courses)) for courses in Course.objects.all()]

    contacts = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )
    courses = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )


class BookinginvoiceAdmin(BaseAdmin):
    form = BookinginvoiceAdminForm
    exclude = ['id', 'created_at', 'updated_at']


admin.site.register(Bookinginvoice, BookinginvoiceAdmin)
