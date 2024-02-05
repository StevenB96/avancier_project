from djongo import models
from bson import ObjectId
from .base_model import BaseModel


class Hotel(BaseModel):
    venue_id = models.CharField(max_length=255, blank=True, null=True)
    address_id = models.CharField(max_length=255, blank=True, null=True)
    hotel_name = models.CharField(max_length=255, blank=True, null=True)
    hotel_website = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Parents
        hotel = self.db['hotel'].find_one({'_id': self.save_value_list["_id"]})
        if hotel:
            self.db['address'].update_one(
                {'_id': ObjectId(hotel["address_id"])},
                {'$set': {'hotel': hotel}}
            )
            venue = self.db['venue'].find_one(
                {'_id': ObjectId(self.save_value_list["venue_id"])})
            self.db['venue'].update_one(
                {'_id': ObjectId(hotel["venue_id"])},
                {'$set': {'hotels': self.update_object_list(
                    venue["hotels"], [hotel])}}
            )

    def __str__(self):
        return str(self.hotel_name) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Hotels'
        db_table = 'hotel'
