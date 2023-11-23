from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewsListCreate.as_view(), name='reviews-list-create-view'),
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroy.as_view(), name='reviews-detail-view')
]
