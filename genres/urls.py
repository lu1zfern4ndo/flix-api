from django.urls import path
from . import views

urlpatterns = [
    path('', views.GenreCreateList.as_view(), name='genre_create_list'),
    path('<int:pk>/', views.GenreRetrieveUpdateDestroy.as_view(), name='genre_retrieve_update_destroy'),
]
