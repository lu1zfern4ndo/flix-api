from django.urls import path
from . import views

urlpatterns = [
    path('', views.genre_create_list, name='genre')
]
