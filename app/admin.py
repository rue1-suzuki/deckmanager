from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import Deck, Event, Organizer


class OrganizerAdmin(UserAdmin):
    list_display = ['username', 'is_active', ]


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'organizer', 'date', ]


class DeckAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'number', 'name', ]


admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Deck, DeckAdmin)
