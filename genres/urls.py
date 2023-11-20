from django.urls import path
from . import views

urlpatterns = [
    path('', views.genre_create_list, name='genre'),
    path('<int:pk>', views.genre_detail, name='genre'),
]
