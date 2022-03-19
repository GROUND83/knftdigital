import imp
from django.urls import path
from . import views

app_name = "authors"

urlpatterns = [
    path("", views.AuthorView.as_view(), name="list"),
    path("<int:pk>/", views.AuthorDetail.as_view(), name="detail"),
]
