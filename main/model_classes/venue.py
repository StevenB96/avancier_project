from django.db import models
from .address import Address
from django.utils import timezone


class Venue(models.Model):
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
    )

    venue_name = models.CharField(max_length=255, blank=True, null=True)
    venue_contact_name = models.CharField(
        max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.venue_name} - {self.id}"

    class Meta:
        verbose_name_plural = 'Venues'
        db_table = 'venue'
        managed = True
