# Generated by Django 2.0.2 on 2018-02-21 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizers', '0004_auto_20180218_1219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizer',
            options={'verbose_name_plural': 'organizers'},
        ),
        migrations.AddField(
            model_name='organizer',
            name='github',
            field=models.URLField(blank=True),
        ),
    ]