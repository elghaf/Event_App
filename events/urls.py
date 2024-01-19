from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", views.home, name="admin"),
    path('members/login_user/', auth_views.LoginView.as_view(), name='login_user'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('add-event/', views.add_event, name='add-event'),
    path('update_event/<event_id>', views.update_event, name='update-event'),
	path('delete_event/<event_id>', views.delete_event, name='delete-event'),
    path("search_events", views.search_events, name="search-events"),
    path("show_event/<int:event_id>", views.show_event, name="show-event"),
	path('events', views.all_events, name="event_lists"),
    path("my_events", views.my_events, name="my-events"),

    path("<int:year>/<str:month>/", views.home, name="home"),

    path('text-event/', views.text_event, name='text-event'),
    path('csv-event/', views.csv_event, name='csv-event'),
    path('pdf-event/', views.pdf_event, name='pdf-event'),


]