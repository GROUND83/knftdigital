import imp
from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.contact, name="contact"),
    path("subscription", views.emailsubscription, name="subscription")
    # path("email/", views.footercontact, name="email"),
]
