from django.db import models
from .contact import Contact
from .course import Course


class Bookinginvoice(models.Model):
    contacts = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
    )
    courses = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )
    description = models.TextField(blank=True, null=True)
    payment_method = models.IntegerField(blank=True, null=True)
    po_or_ref_number = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.description} - {self.id}"

    class Meta:
        verbose_name_plural = 'Bookinginvoices'
        db_table = 'bookinginvoice'
        managed = True
