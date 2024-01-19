
from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields=(("name", "event_date"), "description", "manager", "attendees")
    list_display=("name", "event_date", "manager")
    ordering=("-event_date", "name")
    list_filter=("event_date", "manager")
    search_fields=("name",)