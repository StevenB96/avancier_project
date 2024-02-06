from django.contrib import admin
from .base_admin import BaseAdmin
from django import forms
from django_select2.forms import Select2Widget

from ..model_classes import (
    Certificate,
    CourseCertificate,
    CourseType
)


class CourseCertificateAdminForm(forms.ModelForm):
    class Meta:
        model = CourseCertificate
        fields = '__all__'
        widgets = {
            'certificate': Select2Widget,
            'course_type': Select2Widget
        }
        required = {
            'certificate': False,
            'course_type': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['certificate'].choices = [(certificate.id, str(certificate)) for certificate in Certificate.objects.all()]
        self.fields['course_type'].choices = [(course_type.id, str(course_type)) for course_type in CourseType.objects.all()]

    certificate = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )
    course_type = forms.ChoiceField(
        widget=Select2Widget,
        required=False,
    )


class CourseCertificateAdmin(BaseAdmin):
    form = CourseCertificateAdminForm
    exclude = []


admin.site.register(CourseCertificate, CourseCertificateAdmin)
