from django.urls import path
from . import views

urlpatterns = [
    path('', views.genre_create_list, name='genre'),
    path('<int:pk>/', views.genre_detail_update_delete, name='genre'),
]
