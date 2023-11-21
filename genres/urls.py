from django.urls import path
from . import views

urlpatterns = [
    path('', views.GenreCreateList.as_view(), name='genre'),
    path('<int:pk>/', views.genre_detail_update_delete, name='genre'),
]
