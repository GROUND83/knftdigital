from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
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
                    "file",
                    "thumnail",
                    "file360",
                    "file800",
                )
            },
        ),
    )

    # exclude = (
    #     "thumnail",
    #     "file100",
    #     "file360",
    #     "file800",
    # )

    # def get_thumbnail(self, obj):

    #     type_tuple = guess_type(obj.file.url, strict=True)
    #     if (type_tuple[0]).__contains__("image"):
    #         return mark_safe(f'<img width="50px" src="{obj.file.url}" />')
    #     elif (type_tuple[0]).__contains__("video"):
    #         print(obj.thumnail)
    #         return mark_safe(f'<img width="50px" src="f"{obj.thumnail}" />')

    # get_thumbnail.short_description = "Thumbnail"
