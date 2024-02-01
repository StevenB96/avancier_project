from djongo import models
from .base_model import BaseModel


class Attendee(BaseModel):
    bookinginvoice_id = models.CharField(max_length=255, blank=True, null=True)
    course_id = models.CharField(max_length=255, blank=True, null=True)
    instruction_email_address = models.CharField(
        max_length=255, blank=True, null=True)
    exam_result_email_address = models.CharField(
        max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    instruction_sent_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.name) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Attendees'
        db_table = 'attendee'
