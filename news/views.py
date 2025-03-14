from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import New
from comments.models import Comment
from .serializers import NewSerializer
from comments.serializers import CommentSerializer
from .pagination import NewPagination


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    pagination_class = NewPagination
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views_count += 1
        instance.save(update_fields=['views_count'])
        return super().retrieve(request, *args, **kwargs)

    @action(detail=True, methods=['get'], url_path='comments')
    def comments(self, request, slug=None):
        news = self.get_object()
        comments = Comment.objects.filter(new=news)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='publish')
    def publish(self, request, slug=None):
        news = self.get_object()
        if news.is_published:
            return Response({'detail': 'Новость уже опубликована.'}, status=status.HTTP_400_BAD_REQUEST)
        news.is_published = True
        news.save(update_fields=['is_published'])
        return Response({'detail': 'Новость опубликована!', 'slug': news.slug}, status=status.HTTP_200_OK)