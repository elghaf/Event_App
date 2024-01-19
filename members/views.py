from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import Chef

def login_user(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You were logged in!!"))
            return redirect("home")
        else:
            messages.success(request, ("Username or Password is INCORRECT. Please Try Again!!!!"))
            return redirect("login_user")
    return render(request, "authenticate/login.html", {})


def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'authenticate/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'authenticate/login.html')


from django.contrib.auth.models import Group

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            if form.cleaned_data.get('is_chef'):
                group, created = Group.objects.get_or_create(name='chefs')
            else:
                group, created = Group.objects.get_or_create(name='members')
            user.groups.add(group)
            return redirect('login_user')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {'form': form})


def register_chef(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            if request.user.groups.filter(name='chefs').exists():
                Chef.objects.create(user=request.user)
                return redirect('chef_dashboard')
            else:
                form.add_error(None, 'You do not have permission to register as a chef.')
    else:
        form = ChefRegistrationForm()
    return render(request, 'authenticate/register_user.html', {'form': form})



def logout_user(request):
    # Your logout logic here...
    logout(request)
    return redirect('login_user') 
