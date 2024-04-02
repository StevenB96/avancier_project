from django.db import models
from .course import Course


class Attendee(models.Model):
    courses = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    instruction_email_address = models.CharField(max_length=255, blank=True, null=True)
    exam_result_email_address = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    instruction_sent_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.id}"

    class Meta:
        verbose_name_plural = 'Attendees'
        db_table = 'attendee'
        managed = True
