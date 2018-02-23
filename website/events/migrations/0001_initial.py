# Generated by Django 2.0.2 on 2018-02-22 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('speakers', '__first__'),
        ('supporters', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('photo', models.ImageField(blank=True, upload_to='events/')),
                ('description', models.TextField()),
                ('reg_link', models.URLField(blank=True)),
                ('event_type', models.CharField(choices=[('WORKSHOP', 'Workshop'), ('MEETUP', 'Meetup'), ('HACKATHON', 'Hackathon'), ('CONFERENCE', 'Conference'), ('FESTIVAL', 'Festival')], default='MEETUP', max_length=10)),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speakers.Speaker')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporters.Supporter')),
            ],
            options={
                'verbose_name_plural': 'events',
            },
        ),
    ]
