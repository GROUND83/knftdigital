from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Tag)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = ("name",)

    # def used_by(self, obj):
    #     return obj.rooms.count()

    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "number",
        "author",
    )
    filter_horizontal = ("tags",)
    fieldsets = (
        (
            "기본정보",
            {
                "fields": (
                    "author",
                    "number",
                    "price",
                    "dimensionsx",
                    "dimensionsy",
                    "creationDate",
                )
            },
        ),
        (
            "추가정보",
            {
                "fields": (
                    "projectType",
                    "productType",
                    "projectTitle",
                    "edtionTitle",
                    "otherTitle",
                    "theme",
                    "type",
                )
            },
        ),
        (
            "market_link",
            {
                "fields": (
                    "foundataionLink",
                    "openseaLink",
                    "solahartLink",
                    "raribleLink",
                )
            },
        ),
        (
            "tags",
            {"fields": ("tags",)},
        ),
        (
            "작품",
            {
                "fields": [
                    "image",
                ]
            },
        ),
        (
            "작품내용",
            {
                "fields": [
                    "title",
                    "description",
                ]
            },
        ),
        ("show", {"fields": ("main",)}),
    )
