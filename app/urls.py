from django.urls import path
from app.views import organizer, event, deck

from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'


app_name = 'app'

urlpatterns = [
    path('', Index.as_view(), name='index',),
    path(
        'organizer/create/',
        organizer.Create.as_view(),
        name='organizer_create',
    ),
    path(
        'organizer/list/',
        organizer.List.as_view(),
        name='organizer_list',
    ),
    path(
        'organizer/<int:pk>/detail/',
        organizer.Detail.as_view(),
        name='organizer_detail',
    ),
    path(
        'organizer/<int:pk>/update/',
        organizer.Update.as_view(),
        name='organizer_update',
    ),
    path(
        'organizer/<int:pk>/delete/',
        organizer.Delete.as_view(),
        name='organizer_delete',
    ),
    path(
        'event/create/',
        event.Create.as_view(),
        name='event_create',
    ),
    path(
        'event/list/',
        event.List.as_view(),
        name='event_list',
    ),
    path(
        'event/<uuid:pk>/detail/',
        event.Detail.as_view(),
        name='event_detail',
    ),
    path(
        'event/<uuid:pk>/update/',
        event.Update.as_view(),
        name='event_update',
    ),
    path(
        'event/<uuid:pk>/delete/',
        event.Delete.as_view(),
        name='event_delete',
    ),
    path(
        'event/<uuid:event_uuid>/deck/create/',
        deck.Create.as_view(),
        name='deck_create',
    ),
    path(
        'event/<uuid:event_uuid>/deck/list/',
        deck.List.as_view(),
        name='deck_list',
    ),
    path(
        'event/<uuid:event_uuid>/deck/<uuid:pk>/detail/',
        deck.Detail.as_view(),
        name='deck_detail',
    ),
    path(
        'event/<uuid:event_uuid>/deck/<uuid:pk>/update/',
        deck.Update.as_view(),
        name='deck_update',
    ),
    path(
        'event/<uuid:event_uuid>/deck/<uuid:pk>/delete/',
        deck.Delete.as_view(),
        name='deck_delete',
    ),
]
