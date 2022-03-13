from pyexpat import model
from django.shortcuts import render
from . import models

from django.views.generic import ListView, DetailView

# Create your views here.
class ProductView(ListView):
    model = models.Product
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "products"


class ProductDetail(DetailView):
    model = models.Product

    def get_context_data(self, **kwargs):

        context = super(ProductDetail, self).get_context_data(**kwargs)
        context["otherProducts"] = models.Product.objects.exclude(
            author=self.get_object().author
        )
        print(context)
        return context
