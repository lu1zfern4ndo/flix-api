from django.urls import path
from . import views

urlpatterns = [
    path('', views.GenreCreateList.as_view(), name='genre-create-list-view'),
    path('<int:pk>/', views.GenreRetrieveUpdateDestroy.as_view(), name='genre-detail-view'),
]
