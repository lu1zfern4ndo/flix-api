from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieCreateList.as_view(), name='movies-create-list'),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDetroy.as_view(), name='movies-detail')
]
