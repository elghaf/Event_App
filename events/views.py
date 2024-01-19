from datetime import datetime
import calendar
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from calendar import HTMLCalendar
from .models import Event
from .forms import *

# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
    month=month.capitalize()
    # changing month into integer like january to 1
    month_number = list(calendar.month_name).index(month)
    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    current_year = now.year
    time = now.strftime("%I:%M:%S %p")
    events = Event.objects.filter(event_date__year=year, event_date__month=month_number).order_by("-event_date", "name")
    return render(request, "events/home.html",{"events": events,"year":year, "month":month, "cal":cal,
                                            "current_year":current_year, "time": time, "datetime": now})

def search_events(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            searched = request.POST["searched"]
            if not searched:
                messages.success(request, ("You didn't search anything!!!"))
                return redirect("home")
            events = Event.objects.filter(name__icontains=searched).order_by("-event_date", "name")
            messages.success(request, (f"Results of search \"{searched}\""))
            return render(request, "events/search_events.html", {"searched": searched, "events": events, "datetime": datetime.now()})
        else:
            messages.success(request, ("You need to search first!!!"))
            return redirect("home")
    else:
        messages.success(request, ("You aren't Authorized to Search Events. Please Login/Register First !!!"))
        return redirect("login")

def all_events(request):
    event_lists = Event.objects.all().order_by('-event_date')
    for event in event_lists:
        print(event) 
    return render(request, 'events/event_lists.html', 
        {'event_lists': event_lists})


def show_event(request, event_id):
    if request.user.is_authenticated:
        event = Event.objects.get(pk=event_id)
        return render(request, "events/show_event.html", {"event": event, "datetime": datetime.now()})
    else:
        messages.success(request, ("You aren't Authorized to See Event's Details. Please Login/Register First !!!"))
        return redirect("event_lists")

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Event
from datetime import datetime

def my_events(request):
    if request.user.is_authenticated:
        # Fetch events where the user is the manager
        manager_events_query = Event.objects.filter(manager=request.user)

        print(f"Authenticated user: {request.user}")  # print the authenticated user
        print(f"Manager events query: {manager_events_query}")  # print the manager's events query

        # Fetch events where the user is an attendee
        attendee_events_query = Event.objects.filter(attendees=request.user)

        print(f"Attendee events query: {attendee_events_query}")  # print the attendee's events query

        # Combine and order both sets of events
        events_query = manager_events_query.union(attendee_events_query).order_by("-event_date", "name")

        p = Paginator(events_query, 6)
        page = request.GET.get("page")
        events = p.get_page(page)

        print(f"Events: {events}")  # print the events
        return render(request, "events/my_events.html", {"events": events, "datetime": datetime.now()})
    else:
        messages.success(request, ("You aren't Logged in. Please Login/Register First to view your Events !!!"))
        return redirect("login")




from django.shortcuts import render, redirect
from .forms import EventForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_chef(user):
    return user.groups.filter(name='chefs').exists()


@login_required
def add_event(request):
    if not is_chef(request.user):
        messages.error(request, 'You must be a chef to add an event.')
        return redirect('home')

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            event = form.save(commit=False)
            event.manager = request.user
            event.save()
            print("Event saved")
            return redirect('home')
        else:
            print("Form is not valid")
            print(form.errors)
            messages.error(request, 'There was an error with your submission. Please check your data and try again.')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})



from django.http import HttpResponseForbidden

def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)

    # Check if the user is the chef of the event or a superuser
    if not request.user.is_superuser and request.user != event.chef:
        return HttpResponseForbidden()

    if request.user.is_superuser:
        form = EventFormAdmin(request.POST or None, instance=event)    
    else:
        form = EventForm(request.POST or None, instance=event)
    
    if form.is_valid():
        form.save()
        return redirect('event_lists')

    return render(request, 'events/update_event.html', 
        {'event': event,
        'form':form})
# Delete an Event
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)

    # Check if the user is the chef of the event or a superuser
    if not request.user.is_superuser and request.user != event.chef:
        messages.error(request, ("You Aren't Authorized To Delete This Event!"))
        return redirect('event_lists')

    event.delete()
    messages.success(request, ("Event Deleted!!"))
    return redirect('event_lists')

def text_event(request):
    # Your logic here
    pass


def csv_event(request):
    # Your logic here
    pass

def pdf_event(request):
    # Your logic here
    print("pdf_event")