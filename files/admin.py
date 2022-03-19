from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        "caption",
        "author",
        # "get_thumbnail",
        "content_type",
        "file",
        "thumnail",
        "file360",
        "file800",
    )
    fieldsets = (
        (
            "기본정보",
            {
                "fields": (
                    "author",
                    "content_type",
                    "caption",
                    "file",
                    "thumnail",
                    "file360",
                    "file800",
                )
            },
        ),
    )
