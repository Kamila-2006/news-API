from django.urls import path
from . import views


urlpatterns = [
    path('news/', views.NewListCreateView.as_view(), name='new-list'),
    path('news/<int:pk>/', views.NewDetailView.as_view(), name='new-detail'),
]