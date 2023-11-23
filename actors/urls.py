from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.ActorCreateList.as_view(), name='actor-list-create-view'),
    path('actors/<int:pk>/', views.ActorRetrieveUpdateDestroy.as_view(), name='actor-detail-view')
]
