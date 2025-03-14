from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from comments.views import CommentViewSet


router = DefaultRouter()
router.register(r'news', views.NewViewSet, basename='new')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]