from djongo import models
from .venue import Venue
from .hotel import Hotel
from .bookinginvoice import Bookinginvoice
from .base_model import BaseModel


class Address(BaseModel):
    venue = models.EmbeddedField(model_container=Venue)
    hotel = models.EmbeddedField(model_container=Hotel)
    bookinginvoices = models.ArrayField(model_container=Bookinginvoice)

    building_name = models.CharField(max_length=255, blank=True, null=True)
    building_number_and_thoroughfare_name = models.CharField(
        max_length=255, blank=True, null=True)
    locality_name = models.CharField(max_length=255, blank=True, null=True)
    town_name = models.CharField(max_length=255, blank=True, null=True)
    administrative_area_name = models.CharField(
        max_length=255, blank=True, null=True)
    county_name = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=20)

    def __str__(self):
        return str(self.building_number_and_thoroughfare_name) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Addresses'
        db_table = 'address'
        managed = True
