from django.db import models
from django.utils import timezone
from .venue import Venue
from .address import Address


class Hotel(models.Model):
    venues = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE,
    )
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
    )

    hotel_name = models.CharField(max_length=255, blank=True, null=True)
    hotel_website = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.hotel_name} - {self.id}"

    class Meta:
        verbose_name_plural = 'Hotels'
        db_table = 'hotel'
        managed = True
