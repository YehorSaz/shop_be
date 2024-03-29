import math

from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'size'
    max_page_size = 100

    def get_paginated_response(self, data):
        count = self.page.paginator.count
        total_pages = math.ceil(count / self.get_page_size(self.request))
        return Response({
            'total_items': count,
            'total_pages': total_pages,
            'prev': self.get_previous_link(),
            'next': self.get_next_link(),
            'results': data
        }, status.HTTP_200_OK)
