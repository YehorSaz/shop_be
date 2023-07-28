from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination

from drf_yasg import openapi
from drf_yasg.inspectors import DjangoRestResponsePagination


class PaginationInspector(DjangoRestResponsePagination):

    def get_paginated_response(self, paginator, response_schema):
        assert response_schema.type == openapi.TYPE_ARRAY, "array return expected for paged response"
        paged_schema = None
        if isinstance(paginator, PageNumberPagination):
            paged_schema = openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=OrderedDict((
                    ('total_items', openapi.Schema(type=openapi.TYPE_INTEGER)),
                    ('total_pages', openapi.Schema(type=openapi.TYPE_INTEGER)),
                    ('prev', openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, x_nullable=True)),
                    ('next', openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, x_nullable=True)),
                    ('results', response_schema),
                )),
            )

        return paged_schema
