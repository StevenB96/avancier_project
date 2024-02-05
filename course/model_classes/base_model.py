from pymongo import MongoClient
from django.conf import settings
from djongo import models

default_db_settings = settings.DATABASES['default']
mongo_uri = f"mongodb://{default_db_settings['HOST']}:{default_db_settings['PORT']}/{default_db_settings['NAME']}"


class BaseModel(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        client = MongoClient(mongo_uri)
        self.db = client[default_db_settings['NAME']]

    _id = models.ObjectIdField(primary_key=True, db_column='_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        exclude_fields = []
        self.save_value_list = {
            field.name: getattr(self, field.name) for field in self._meta.fields
            if getattr(self, field.name) is not None and
            field.name not in exclude_fields
        }


    def get_document_by_chaining(self, chain):
        # current_id = self.save_value_list["_id"]
        # for document in chain:
        #     venue = self.db[document].find_one({'_id': self.save_value_list["_id"]})
        #     current_id = 
        pass


    def update_object_list(self, array1, array2):
        if not (isinstance(array1, list) and isinstance(array2, list)):
            print("Both array1 and array2 should be of type list.")
            return []

        # If either array is empty, return the other one
        if not array1:
            return array2
        if not array2:
            return array1

        # Create a set to keep track of unique objects based on a hashable representation
        unique_objects = set()

        # Helper function to create a hashable representation of a dictionary
        def dict_to_tuple(d):
            return tuple(sorted(d.items()))

        # Iterate over array1 and add objects to the set
        for obj in array1:
            unique_objects.add(dict_to_tuple(obj))

        # Iterate over array2 and update existing objects or add new ones to the set
        for obj in array2:
            unique_objects.add(dict_to_tuple(obj))

        # Convert the set back to a list of dictionaries
        merged_objects = [dict(item) for item in unique_objects]

        return merged_objects

    class Meta:
        managed = False
        abstract = True
