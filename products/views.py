from pyexpat import model
from django.shortcuts import render
from . import models, forms
from authors.models import Author
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, FormView, View

# Create your views here.
class ProductView(ListView):
    template_name = "products/product_list.html"
    model = models.Product
    # paginate_by = 9
    # paginate_orphans = 5
    ordering = "title"
    context_object_name = "products"

    def get_queryset(self):
        print("서치", self.request.GET)
        queryset = super().get_queryset()
        queryset.order_by("title")
        sort = int(self.request.GET.get("sort", 0))
        artist = int(self.request.GET.get("artists", 0))
        project_type = int(self.request.GET.get("project_type", 0))
        searchtext = self.request.GET.get("searchtext", "")
        type = int(self.request.GET.get("type", 0))

        filter_args = {}

        # if title != "":
        #     filter_args["title__icontains"] = title

        if artist != 0:
            filter_args["author__pk"] = artist
        if project_type != 0:
            filter_args["project_type__pk"] = project_type
        if type != 0:
            filter_args["type__pk"] = type

        queryset = queryset.filter(**filter_args)

        if sort == 0:
            # filter_args["type__pk"] = type
            queryset = queryset.order_by("-creationDate")
        elif sort == 1:
            queryset = queryset.order_by("creationDate")
        elif sort == 2:
            # filter_args["type__pk"] = type
            queryset = queryset.order_by("price")
        elif sort == 3:
            queryset = queryset.order_by("-price")

        if searchtext != "":
            queryset = (
                queryset.filter(title__icontains=searchtext)
                | queryset.filter(description__icontains=searchtext)
                | queryset.filter(tags__name__icontains=searchtext)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        projectTypes = models.ProjectType.objects.all()
        types = models.Type.objects.all()
        artist = Author.objects.all()

        # products = models.Product.objects.all()
        # print(filter_set)
        title = self.request.GET.get("title", "")
        # author = self.request.GET.get("author", "")
        # print(author)
        project_type = int(self.request.GET.get("project_type", 0))
        artist_name = int(self.request.GET.get("artists", 0))
        type = int(self.request.GET.get("type", 0))
        sort = int(self.request.GET.get("sort", 0))
        price = int(self.request.GET.get("price", 3))
        searchtext = self.request.GET.get("searchtext", "")
        form = {
            "title": title,
            "s_project_types": project_type,
            "s_types": type,
            "s_artists": artist_name,
            "sort": sort,
            "price": price,
            "searchtext": searchtext,
        }
        context["count"] = models.Product.objects.all().count
        context["project_types"] = projectTypes
        context["artists"] = artist
        context["types"] = types
        context["form"] = form
        user_agent = self.request.META["HTTP_USER_AGENT"]
        keywords = ["Mobile", "Opera Mini", "Android"]
        if self.request.user_agent.is_mobile:
            context["is_mobile"] = True
        else:
            context["is_mobile"] = False
        return context


class ProductDetail(DetailView):
    model = models.Product

    def get_context_data(self, **kwargs):

        context = super(ProductDetail, self).get_context_data(**kwargs)
        context["otherProducts"] = models.Product.objects.exclude(
            author=self.get_object().author
        )[:6]
        # print(context)
        return context


class tagSearch(DetailView):
    def get(self, request, tag):
        # ======== HERE, TITLE IS ACTUALLY urltitle! ==================
        print(tag, request)
        products = models.Product.objects.filter(tags__id=tag)
        tag = models.Tag.objects.get(id=tag)
        return render(request, "search_result.html", {"products": products, "tag": tag})


# def search(request):
#     print("ㅅㅓ치시작", request.GET)
#     title = request.GET.get("title", "")
#     project_type = int(request.GET.get("project_type", 0))
#     type = int(request.GET.get("type", 0))
#     createdAt = int(request.GET.get("createdAt", 0))
#     price = int(request.GET.get("price", 0))
#     form = {
#         "title": title,
#         "s_project_types": project_type,
#         "s_types": type,
#         "createdAt": createdAt,
#         "price": price,
#     }
#     projectTypes = models.ProjectType.objects.all()
#     print(form)
#     types = models.Type.objects.all()
#     choices = {
#         "project_types": projectTypes,
#         "types": types,
#     }
#     filter_args = {}
#     if title != "":
#         filter_args["title__startswith"] = title
#     if project_type != 0:
#         filter_args["project_type__pk"] = project_type
#     if type != 0:
#         filter_args["type__pk"] = type
#     products = []
#     if createdAt is True:
#         # filter_args["type__pk"] = type
#         products = models.Product.objects.filter(**filter_args).order_by(
#             "-creationDate"
#         )
#     else:
#         products = models.Product.objects.filter(**filter_args).order_by("creationDate")
#     if price is True:
#         # filter_args["type__pk"] = type
#         products = models.Product.objects.filter(**filter_args).order_by("-price")
#     else:
#         products = models.Product.objects.filter(**filter_args).order_by("price")

#     # if len(s_project_types) > 0:
#     #     for s_project_type in s_project_types:
#     #         filter_args["project_types__pk"] = int(s_project_type)

#     print(products)
#     print("ㅅㅓ치끝")
#     return render(
#         request, "products/search.html", {**form, **choices, "products": products}
#     )


# class SearchView(View):

#     """SearchView Definition"""

#     def get(self, request):

#         title = request.GET.get("title")

#         if title:

#             form = forms.SearchForm(request.GET)

#             if form.is_valid():

#                 title = form.cleaned_data.get("title")

#                 project_type = form.cleaned_data.get("project_type")

#                 filter_args = {}

#                 if title != "all":
#                     filter_args["title__startswith"] = title

#                 filter_args["title"] = title

#                 if project_type is not None:
#                     filter_args["projectType"] = project_type

#                 qs = models.Product.objects.filter(**filter_args).order_by("-created")
#                 wholeProduct = models.Product.objects.all()
#                 paginator = Paginator(qs, 10, orphans=5)

#                 page = request.GET.get("page", 1)

#                 products = paginator.get_page(page)
#                 print(wholeProduct.count)
#                 return render(
#                     request,
#                     "products/search.html",
#                     {"form": form, "products": products, "wholeProduct": wholeProduct},
#                 )

#         else:
#             form = forms.SearchForm()
#             wholeProduct = models.Product.objects.all()

#         return render(
#             request,
#             "products/search.html",
#             {"form": form, "wholeProduct": wholeProduct},
#         )
