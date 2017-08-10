from rest_framework import serializers
from .models import Speaker, Supporter, Event, Organizer


class SpeakerSerializer(serializers.ModelSerializer):
    latest_event = serializers.SerializerMethodField()

    class Meta:
        model = Speaker
        fields = ('name', 'photo', 'company', 'designation', 'contact_number',
                  'email_id', 'social_link', 'latest_event')

    def get_latest_event(self, obj):
        if obj.event_set:
            latest_event = obj.event_set.first()
            data = {'id': latest_event.id, 'name': latest_event.name}
            return data
        return None


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    venue = serializers.SerializerMethodField()
    speakers = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_venue(self, obj):
        return obj.venue.address

    def get_speakers(self, obj):
        return obj.speakers.values_list('name', flat=True)


class SupporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supporter
        fields = '__all__'
