import imp
from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.ProductView.as_view(), name="productList"),
    # path("", views.ProductView.as_view(), name="productList"),
    path("<int:pk>", views.ProductDetail.as_view(), name="detail"),
    path("tag/<int:tag>", views.tagSearch.as_view(), name="tagSearch"),
    path("search/", views.search, name="search"),
]
