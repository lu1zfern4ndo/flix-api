from django.urls import path
from . import views

urlpatterns = [
    path('', views.ActorCreateList.as_view(), name='actor-list-create-view'),
    path('<int:pk>/', views.ActorRetrieveUpdateDestroy.as_view(), name='actor-detail-view')
]
