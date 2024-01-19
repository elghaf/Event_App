from django import forms
from django.forms import ModelForm
from .models import Event

class EventFormAdmin(ModelForm):
    class Meta:
        model = Event
        fields = ("name", "event_date", "manager", "attendees", "description")
        labels = {
            "name": "",
            "event_date": "",
            "manager": "Manager",
            "attendees": "Attendees",
            "description": ""
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": 'form-control', "placeholder": "Enter Your Event Name"}),
            "event_date": forms.DateInput(attrs={"class": 'form-control', "placeholder": "Enter Event Date (YYYY-MM-DD)"}),
            "manager": forms.Select(attrs={"class": 'form-select', "placeholder": "Enter Manager"}),
            "attendees": forms.SelectMultiple(attrs={"class": 'form-control select2', "placeholder": "Select Collaborateurs"}),
            "description": forms.Textarea(attrs={"class": 'form-control', "placeholder": "Enter Description"})
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ("name", "event_date", "attendees", "description")
        labels = {
            "name": "",
            "event_date": "",
            "attendees": "Attendees",
            "description": ""
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": 'form-control', "placeholder": "Enter Your Event Name"}),
            "event_date": forms.DateInput(attrs={"class": 'form-control', "placeholder": "Enter Event Date (YYYY-MM-DD)"}),
            "attendees": forms.SelectMultiple(attrs={"class": 'form-control select2', "placeholder": "Select Collaborateurs"}),
            "description": forms.Textarea(attrs={"class": 'form-control', "placeholder": "Enter Description"})
        }
