from django.utils import timezone
from django.db import models


class BaseModel(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
