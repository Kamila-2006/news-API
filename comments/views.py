from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from .pagination import CommentsPagination


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CommentsPagination