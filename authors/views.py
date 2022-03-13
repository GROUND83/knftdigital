from pyexpat import model
from django.shortcuts import render
from . import models

from django.views.generic import ListView, DetailView

# Create your views here.
class AuthorView(ListView):
    model = models.Author
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "authors"


class AuthorDetail(DetailView):
    model = models.Author
