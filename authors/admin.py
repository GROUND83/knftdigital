from django.contrib import admin
from . import models
from django import forms
from django.utils.safestring import mark_safe


# Register your models here.


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ["headshot_image"]

    def headshot_image(self, obj):
        return mark_safe(
            '<img src="/media/{url}" width="100" height="100" />'.format(
                url=obj.avatar_thumbnail,
            )
        )

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
                    "headshot_image",
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
