from django.db import models


class SocialLinks(models.Model):
    facebook = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    google_plus = models.URLField(max_length=200, blank=True)

    class Meta:
        abstract = True
