from django.db import models
from .address import Address


class Venue(models.Model):
    # RELATIONSHIPS
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
    )
    # ATTRIBUTES FIELDS
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.id}"

    class Meta:
        verbose_name_plural = 'Venues'
        db_table = 'venue'
        managed = True
