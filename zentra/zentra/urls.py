from django.urls import path
from django.urls import include
from django.contrib import admin


urlpatterns = [
    path('',include('home.urls')),
    path('admin/', admin.site.urls),
]
