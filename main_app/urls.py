from django.conf.urls import url
from .views import SpeakerListView, OrganizerListView, EventListView, \
    SupporterListView


urlpatterns = [
    url(r'^speakers/$', SpeakerListView.as_view()),
    url(r'^supporters/$', SupporterListView.as_view()),
    url(r'^events/$', EventListView.as_view()),
    url(r'^organizers/$', OrganizerListView.as_view()),
]
