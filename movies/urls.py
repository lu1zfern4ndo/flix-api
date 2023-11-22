from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieCreateList.as_view(), name='movies-create-list'),
    path('<int:pk>/', views.MovieRetrieveUpdateDetroy.as_view(), name='movies-detail')
]
