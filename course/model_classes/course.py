from djongo import models
from .bookinginvoice import Bookinginvoice
from .attendee import Attendee
from .base_model import BaseModel


class Course(BaseModel):
    bookinginvoices = models.ArrayField(model_container=Bookinginvoice)
    attendees = models.ArrayField(model_container=Attendee)

    venue_id = models.CharField(max_length=255, blank=True, null=True)
    course_type_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    attendee_total = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.description) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Courses'
        db_table = 'course'
