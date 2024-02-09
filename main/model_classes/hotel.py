from django.db import models
from .venue import Venue
from .address import Address


class Hotel(models.Model):
    # RELATIONSHIPS
    venues = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE,
    )
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    # ATTRIBUTES FIELDS
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.id}"

    class Meta:
        verbose_name_plural = 'Hotels'
        db_table = 'hotel'
        managed = True
