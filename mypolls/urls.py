from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('polls/',include('polls.urls')),
    path('user/',include('user.urls')),
    path('admin/', admin.site.urls),
]
