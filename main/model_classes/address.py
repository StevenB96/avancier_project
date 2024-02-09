from django.db import models
from django.utils import timezone

class Address(models.Model):
    # ATTRIBUTES FIELDS
    building_name = models.CharField(max_length=255, blank=True, null=True)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    post_code = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.building_name} - {self.id}"

    class Meta:
        verbose_name_plural = 'Addresses'
        db_table = 'address'
        managed = True
