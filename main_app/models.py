from django.db import models
from django.core.validators import RegexValidator


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Format: '+999999999'")


class Organizer(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20, validators=[phone_regex])
    email_id = models.EmailField(max_length=255)


class Supporter(models.Model):
    name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20, validators=[phone_regex])
    email_id = models.EmailField(max_length=255)
    is_active = models.BooleanField(default=True)
    website = models.URLField(null=True, blank=True)


class Speaker(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20, validators=[phone_regex])
    email_id = models.EmailField(max_length=255)


class Event(models.Model):
    name = models.CharField(max_length=200)
    event_type = models.CharField(max_length=50)
    technology = models.CharField(max_length=50)
    date = models.DateField()
    venue = models.CharField(max_length=200)
    description = models.TextField()
    registration_link = models.URLField()
    speaker = models.ForeignKey(Speaker)
