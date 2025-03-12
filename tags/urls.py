from django.urls import path
from . import views


urlpatterns = [
    path('tags/', views.TagListCreateView.as_view(), name='tag-list'),
    path('tags/<str:slug>/', views.TagDetailView.as_view(), name='tag-detail'),
]