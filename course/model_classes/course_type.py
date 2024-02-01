from djongo import models
from .enquiry import Enquiry
from .course import Course
from .certificate import Certificate
from .base_model import BaseModel


class CourseType(BaseModel):
    enquiries = models.ArrayField(model_container=Enquiry)
    courses = models.ArrayField(model_container=Course)
    certificates = models.ArrayField(model_container=Certificate)

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    delivery_mode = models.IntegerField(blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.name) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Course Types'
        db_table = 'course_type'
        managed = True
