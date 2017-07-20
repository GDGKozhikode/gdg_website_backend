from rest_framework.generics import ListCreateAPIView
from .serializers import SpeakerSerializer, SupporterSerializer, \
    EventSerializer, OrganizerSerializer
from .models import Speaker, Organizer, Supporter, Event


class SpeakerListView(ListCreateAPIView):
    serializer_class = SpeakerSerializer
    queryset = Speaker.objects.all()
    allowed_methods = ('GET',)


class OrganizerListView(ListCreateAPIView):
    serializer_class = OrganizerSerializer
    queryset = Organizer.objects.all()
    allowed_methods = ('GET',)


class EventListView(ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    allowed_methods = ('GET',)


class SupporterListView(ListCreateAPIView):
    serializer_class = SupporterSerializer
    queryset = Supporter.objects.all()
    allowed_methods = ('GET',)
