# pagination.py
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 4  # Default page size
    page_size_query_param = 'page_size'  # Allows overriding via query params
    max_page_size = 100
