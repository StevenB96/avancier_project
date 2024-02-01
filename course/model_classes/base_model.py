from djongo import models


class BaseModel(models.Model):
    _id = models.ObjectIdField(primary_key=True, db_column='_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        abstract = True
