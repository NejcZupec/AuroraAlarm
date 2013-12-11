from django.db import models
from photologue.models import ImageModel

class PhotoWithLocation(ImageModel):
    longitude = models.DecimalField(max_digits=20, decimal_places=17, default=0.0)
    latitude = models.DecimalField(max_digits=20, decimal_places=17, default=0.0)
