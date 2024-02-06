from django.db import models
from django.utils import timezone
from .bookinginvoice import Bookinginvoice
from .course import Course


class Attendee(models.Model):
    bookinginvoices = models.ForeignKey(
        Bookinginvoice,
        on_delete=models.CASCADE,
    )
    courses = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )

    instruction_email_address = models.CharField(
        max_length=255, blank=True, null=True)
    exam_result_email_address = models.CharField(
        max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    instruction_sent_date = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.id}"

    class Meta:
        verbose_name_plural = 'Attendees'
        db_table = 'attendee'
        managed = True
