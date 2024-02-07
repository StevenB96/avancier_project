from django.db import models
from django.utils import timezone

class Address(models.Model):
    building_name = models.CharField(max_length=255, blank=True, null=True)
    building_number_and_thoroughfare_name = models.CharField(
        max_length=255, blank=True, null=True)
    locality_name = models.CharField(max_length=255, blank=True, null=True)
    town_name = models.CharField(max_length=255, blank=True, null=True)
    administrative_area_name = models.CharField(
        max_length=255, blank=True, null=True)
    county_name = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.building_number_and_thoroughfare_name} - {self.id}"

    class Meta:
        verbose_name_plural = 'Addresses'
        db_table = 'address'
        managed = True
