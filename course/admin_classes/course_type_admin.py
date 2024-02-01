from django.contrib import admin

from ..model_classes import (
    CourseType,
)


class CourseTypeAdmin(admin.ModelAdmin):
    exclude = ['_id', 'enquiries', 'courses', 'certificates']


admin.site.register(CourseType, CourseTypeAdmin)
