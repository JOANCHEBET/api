from django.urls import path
from .views import ProductDetail, ProductList
urlpatterns=[
    path('products/', ProductList.as_view(), name='product')
]