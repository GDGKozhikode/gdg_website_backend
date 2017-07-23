from django.db import models
from django.core.validators import RegexValidator


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Format: '+999999999'")


class SocialLink(models.Model):
    facebook = models.URLField(null=True, blank=True)
    google_plus = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)


class Location(models.Model):
    address = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=12, decimal_places=10)
    longitude = models.DecimalField(max_digits=13, decimal_places=10)


class Organizer(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20, validators=[phone_regex])
    email_id = models.EmailField(max_length=255)
    photo = models.ImageField(upload_to='images/organizers', null=True,
                              blank=True)
    social_link = models.ForeignKey(SocialLink)
    ok_to_contact = models.BooleanField(default=False)


class Supporter(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/supporters', null=True,
                              blank=True)
    is_active = models.BooleanField(default=True)
    website = models.URLField(null=True, blank=True)
    location = models.ForeignKey(Location)


class Speaker(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/speakers', null=True,
                              blank=True)
    company = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20, validators=[phone_regex])
    email_id = models.EmailField(max_length=255)
    social_link = models.ForeignKey(SocialLink)


class Event(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/events', null=True, blank=True)
    event_type = models.CharField(max_length=50)
    technology = models.CharField(max_length=50)
    date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    venue = models.ForeignKey(Location)
    description = models.TextField()
    registration_link = models.URLField()
    speaker = models.ForeignKey(Speaker)


class EventImage(models.Model):
    event = models.ForeignKey(Event)
    image = models.ImageField(upload_to='images/events')


class SupportFile(models.Model):
    event = models.ForeignKey(Event)
    file = models.FileField(upload_to='supportfiles')
