from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewsListCreate.as_view(), name='reviews-list-create-view'),
    path('<int:pk>/', views.ReviewRetrieveUpdateDestroy.as_view(), name='reviews-detail-view')
]
