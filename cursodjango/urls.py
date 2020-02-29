from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from aula4.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('aula3.urls')),
    path("aula4", index),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
