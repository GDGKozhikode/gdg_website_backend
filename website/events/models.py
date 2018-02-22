from django.db import models
from speakers.models import Speaker
from supporters.models import Supporter


class Event(models.Model):
    name = models.CharField(max_length=500, blank=False)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    venue = models.ForeignKey(Supporter, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='events/', blank=True)
    description = models.TextField()
    reg_link = models.URLField(max_length=200, blank=True)

    WORKSHOP = 'WORKSHOP'
    MEETUP = 'MEETUP'
    HACKATHON = 'HACKATHON'
    CONFERENCE = 'CONFERENCE'
    FESTIVAL = 'FESTIVAL'
    TYPE = (
        (WORKSHOP, 'Workshop'),
        (MEETUP, 'Meetup'),
        (HACKATHON, 'Hackathon'),
        (CONFERENCE, 'Conference'),
        (FESTIVAL, 'Festival'),
    )
    event_type = models.CharField(max_length=10,
                                  choices=TYPE,
                                  default=MEETUP)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "events"
