from django.urls import path
from .views import index, setacookie, redireciona, show_code, show_get_values, show_post_values

app_name = 'aula3'

urlpatterns = [
    path('', index),
    path('cookie',setacookie),
    path('uol',redireciona),
    path('<int:code>', show_code),
    path('get', show_get_values),
    path('post', show_post_values),
]