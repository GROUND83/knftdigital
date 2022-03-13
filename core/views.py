from itertools import product
from pyexpat import model
from django.shortcuts import render
from products.models import Product
from django.forms.models import model_to_dict

# Create your views here.
def get_product(request):

    firtModel = Product.objects.order_by("?").first()
    main_product = Product.objects.filter(main=True)
    print(vars(main_product))
    return render(
        request,
        "main.html",
        context={"main_product": main_product, "first_product": firtModel},
    )

    # qs=None -- do some here when qs is not found


def about(request):

    return render(request, "about.html")


def contact(request):

    return render(request, "contact.html")
