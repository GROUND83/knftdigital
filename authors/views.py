from itertools import product
from pyexpat import model

# from warnings import filters
from django.shortcuts import render
from . import models
from products.models import Product
from django.views.generic import ListView, DetailView

# Create your views here.
class AuthorView(ListView):
    template_name = "authors/author_list.html"
    model = models.Author
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    # context_object_name = "authors"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_set = models.Author.objects.all()
        print(filter_set)
        if self.request.GET.get("q"):
            name = self.request.GET.get("q")
            print(name)
            filter_set = filter_set.filter(name__contains=name)

        print(context)
        context["authors"] = filter_set
        return context


class AuthorDetail(DetailView):
    model = models.Author

    template_name = "authors/author_detail.html"

    def get_context_data(self, **kwargs):
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        author = self.get_object()
        products = Product.objects.filter(author_name=author.name)
        print(products)
        count = products.count()
        print(count)
        product = products.filter(product_type="project")
        edition = products.filter(product_type="edition")
        others = products.filter(product_type="other")
        print(product)
        context["count"] = count
        context["projects"] = product
        context["editions"] = edition
        context["others"] = others
        return context
