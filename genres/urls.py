from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.GenreCreateList.as_view(), name='genre-create-list-view'),
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroy.as_view(), name='genre-detail-view'),
]
