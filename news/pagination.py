from rest_framework.pagination import PageNumberPagination


class NewPagination(PageNumberPagination):
    page_size = 10