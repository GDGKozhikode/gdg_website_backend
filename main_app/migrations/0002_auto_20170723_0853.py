# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/events'),
        ),
        migrations.AddField(
            model_name='organizer',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/organizers'),
        ),
        migrations.AddField(
            model_name='speaker',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/speakers'),
        ),
        migrations.AddField(
            model_name='supporter',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/supporters'),
        ),
    ]