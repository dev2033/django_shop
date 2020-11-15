from django.urls import path

from .api_views import (
    CategoryListApiView,
    CustomersListAPIView
)

urlpatterns = [
    path('categories/', CategoryListApiView.as_view(), name='categories_list'),
    path('customers/', CustomersListAPIView.as_view(), name='customers_list'),
]
