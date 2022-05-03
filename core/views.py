from itertools import product
from pyexpat import model
from django.shortcuts import render
from products.models import Product
from authors.models import Author


# Create your views here.
def get_product(request):

    firtModel = Product.objects.order_by("?").first()
    main_product = Product.objects.filter(main=True)[:6]

    mindsets = Product.objects.filter(author=11)[:6]

    return render(
        request,
        "main.html",
        context={
            "main_product": main_product,
            "first_product": firtModel,
            "mindsets": mindsets,
        },
    )

    # qs=None -- do some here when qs is not found


def about(request):

    authors = Author.objects.all()

    return render(request, "about.html", context={"authors": authors})


def license(request):

    return render(request, "license.html")
