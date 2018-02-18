from django.core.validators import RegexValidator
from django.db import models
from social.models import SocialLinks


class Organizer(SocialLinks):
    name = models.CharField(max_length=50, blank=False)

    ORGANISER = "ORG"
    CONTRIBUTOR = "CON"

    DESIGINATION = (
        (ORGANISER, 'organiser'),
        (CONTRIBUTOR, 'contributor')
    )

    desigination = models.CharField(max_length=3,
                                    choices=DESIGINATION,
                                    default=CONTRIBUTOR)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Format: '+91999111999'")
    contact_no = models.CharField(max_length=15,
                                  validators=[phone_regex],
                                  blank=False)

    email = models.EmailField(max_length=70, blank=False, unique=True)

    photo = models.ImageField(upload_to='organisers/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
            verbose_name_plural = "organizers"
