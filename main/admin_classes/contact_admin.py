from django.contrib import admin
from .base_admin import BaseAdmin
from django import forms
from django_select2.forms import Select2Widget

from ..model_classes import (
    Company,
    Address,
    Contact
)


class ContactAdminForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'companies': Select2Widget,
            'address': Select2Widget
        }
        required = {
            'companies': False,
            'address': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['companies'].choices = [
            (company.id, str(company))
            for company in Company.objects.all()]
        self.fields['address'].choices = [
            (adress.id, str(adress))
            for adress in Address.objects.all()]


class ContactAdmin(BaseAdmin):
    form = ContactAdminForm
    exclude = ['id', 'created_at', 'updated_at']


admin.site.register(Contact, ContactAdmin)
