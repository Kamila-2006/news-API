from rest_framework import viewsets
from .models import New
from .serializers import NewSerializer
from .pagination import NewPagination


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    pagination_class = NewPagination
    lookup_field = 'slug'