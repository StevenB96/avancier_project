from django.contrib import admin
from .base_admin import BaseAdmin
from django import forms
from django_select2.forms import Select2Widget

from ..model_classes import (
    Enquiry,
    Party,
    CourseType
)


class EnquiryAdminForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'
        widgets = {
            'course_type_id': Select2Widget,
            'party_id': Select2Widget
        }
        required = {
            'course_type_id': False,
            'party_id': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['course_type_id'].choices = [(course_type._id, str(
            course_type)) for course_type in CourseType.objects.all()]
        self.fields['party_id'].choices = [(party._id, str(
            party)) for party in Party.objects.all()]

    course_type_id = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )
    party_id = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )


class EnquiryAdmin(BaseAdmin):
    form = EnquiryAdminForm
    exclude = ['_id']


admin.site.register(Enquiry, EnquiryAdmin)
