# pagination.py
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 4  # Default page size
    page_size_query_param = 'page_size'  # Allows overriding via query params
    max_page_size = 100

    def get_paginated_response(self, data):
        total_pages = math.ceil(self.page.paginator.count / self.page_size)
        
        return Response({
            'count': self.page.paginator.count,  # Total number of items
            'next': self.get_next_link(),        # Link to next page
            'previous': self.get_previous_link(),# Link to previous page
            'total_pages': total_pages,          # Total pages
            'results': data                      # Data of current page
        })