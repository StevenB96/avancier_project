from django.db import models
from django.utils import timezone
from .party import Party
from .address import Address
from .course import Course


class Bookinginvoice(models.Model):
    parties = models.ForeignKey(
        Party,
        on_delete=models.CASCADE,
    )
    address = models.OneToOneField(
        Address,
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

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.description} - {self.id}"

    class Meta:
        verbose_name_plural = 'Bookinginvoices'
        db_table = 'bookinginvoice'
        managed = True
