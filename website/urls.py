from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("events.urls")),
    path("members/", include("members.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header="Club Administration"
admin.site.site_title="Club Administration"
admin.site.index_title="Welcome to Admin Section"