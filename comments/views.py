from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from .pagination import CommentsPagination


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CommentsPagination

    @action(detail=True, methods=['put'], url_path='approve')
    def approve(self, request, pk=None):
        comment = self.get_object()
        if comment.is_approved:
            return Response({'detail': 'Комментарий уже одобрен.'}, status=status.HTTP_400_BAD_REQUEST)
        comment.is_approved = True
        comment.save(update_fields=['is_approved'])
        return Response({'detail': 'Комментарий одобрен!', 'id': comment.id}, status=status.HTTP_200_OK)