from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .serializers import (
    CategorySerializer,
    CustomerSerializer,

)
from ..models import Category, Customer


class CategoryPagination(PageNumberPagination):
    """Пагинация"""
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 10

# Метод переопределения ключей
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('objects_count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('items', data)
        ]))


class CategoryListApiView(ListAPIView):
    """Список категорий в представлении API"""

    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    queryset = Category.objects.all()


class CustomersListAPIView(ListAPIView):
    """Список покупателей в представлении API"""

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
