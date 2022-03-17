from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "type",
        "helpType",
        "email",
        "name",
        "message",
    )
    fieldsets = (
        (
            "기본정보",
            {
                "fields": (
                    "type",
                    "helpType",
                    "email",
                    "name",
                    "message",
                )
            },
        ),
    )
