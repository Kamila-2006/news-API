from rest_framework import generics
from .models import New
from .serializers import NewSerializer
from .pagination import NewPagination


class NewListCreateView(generics.ListCreateAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    pagination_class = NewPagination

class NewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer