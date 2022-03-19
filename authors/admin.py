from django.contrib import admin
from . import models
from django import forms
from django.utils.safestring import mark_safe


# Register your models here.


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "id",
    )

    filter_horizontal = ("products",)
    fieldsets = (
        (
            "기본정보",
            {
                "fields": (
                    "name",
                    "authDes",
                )
            },
        ),
        (
            "추가정보",
            {
                "fields": (
                    "avator",
                    "desTitle",
                    "description",
                )
            },
        ),
        (
            "소셜",
            {
                "fields": (
                    "discord",
                    "facebook",
                    "instargram",
                    "twitter",
                )
            },
        ),
        (
            "작품",
            {
                "fields": [
                    "products",
                ]
            },
        ),
        ("show", {"fields": ("show",)}),
    )
