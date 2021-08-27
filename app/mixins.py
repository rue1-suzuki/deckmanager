from django.contrib.auth.mixins import UserPassesTestMixin

from app.models import Deck, Event
from app.models.organizer import Organizer


class MyOrganizerMixin(UserPassesTestMixin):
    raise_exception = False

    def test_func(self):
        organizer = Organizer.objects.get(pk=self.kwargs['pk'])
        return organizer == self.request.user


class MyEventMixin(UserPassesTestMixin):
    raise_exception = False

    def test_func(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            pk = self.kwargs.get('event_uuid')
        event = Event.objects.get(pk=pk)
        return event.organizer == self.request.user


class MyDeckMixin(UserPassesTestMixin):
    raise_exception = False

    def test_func(self):
        deck = Deck.objects.get(pk=self.kwargs['pk'])
        return deck.event.organizer == self.request.user
