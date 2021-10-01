
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from app.router import app_url


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(app_url))
]
