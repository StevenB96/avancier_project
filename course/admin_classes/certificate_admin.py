from django.contrib import admin
from .base_admin import BaseAdmin
from django import forms
from django_select2.forms import Select2Widget


from ..model_classes import (
    CourseType,
    Certificate,
)


class CertificateAdminForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'
        widgets = {
            'course_type': Select2Widget,
        }
        required = {
            'course_type': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['course_type'].choices = [(course_type.id, str(
            course_type)) for course_type in CourseType.objects.all()]

    course_type = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )


class CertificateAdmin(BaseAdmin):
    form = CertificateAdminForm
    exclude = []


admin.site.register(Certificate, CertificateAdmin)
