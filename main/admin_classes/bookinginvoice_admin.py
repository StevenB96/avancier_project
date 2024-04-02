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
            (contact.id, str(contact))
            for contact in Contact.objects.all()]
        self.fields['courses'].choices = [
            (course.id, str(course))
            for course in Course.objects.all()]


class BookinginvoiceAdmin(BaseAdmin):
    form = BookinginvoiceAdminForm
    exclude = ['id', 'created_at', 'updated_at']


admin.site.register(Bookinginvoice, BookinginvoiceAdmin)
