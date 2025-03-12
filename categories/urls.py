from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<str:slug>/', views.CategoryDetailView.as_view(), name='category-detail'),
]