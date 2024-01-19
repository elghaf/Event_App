from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

def get_superuser():
    superuser = User.objects.filter(is_superuser=True).first()
    if superuser:
        return superuser.id
    return None


class Event(models.Model):
    name = models.CharField("Event Name", max_length=200)
    event_date = models.DateTimeField("Event Date")
    manager = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=get_superuser, related_name="manager")
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(User, blank=True, related_name="attendees")

    def __str__(self):
        return self.name