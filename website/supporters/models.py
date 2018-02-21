from django.db import models
from geoposition.fields import GeopositionField


class Supporter(models.Model):
    name = models.CharField(max_length=50, blank=False)
    photo = models.ImageField(upload_to='supporters/', blank=False)
    location = GeopositionField()
    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "supporters"
