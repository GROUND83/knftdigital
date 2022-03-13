import sys
from django.db import models
from core import models as core_models
from django.utils.safestring import mark_safe
import os.path


# Create your models here.
class Author(core_models.TimeStampedModel):
    class Meta:
        verbose_name = "작가"
        verbose_name_plural = "작가모음"
        ordering = ["name"]

    name = models.CharField(max_length=50, null=True, verbose_name="작가명", unique=True)
    authDes = models.CharField(
        max_length=50, null=True, verbose_name="작가설명", unique=False
    )
    avator = models.ForeignKey(
        "files.File", related_name="files", on_delete=models.CASCADE, null=True
    )

    desTitle = models.CharField(
        max_length=50, null=True, verbose_name="작가 타이틀", unique=False
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="작가 컨텐츠",
    )

    discord = models.CharField(
        max_length=50, null=True, verbose_name="discord", unique=False, blank=True
    )
    facebook = models.CharField(
        max_length=50, null=True, verbose_name="facebook", unique=False, blank=True
    )
    instargram = models.CharField(
        max_length=50, null=True, verbose_name="instargram", unique=False, blank=True
    )
    twitter = models.CharField(
        max_length=50, null=True, verbose_name="twitter", unique=False, blank=True
    )
    show = models.BooleanField(default=True, verbose_name="노출")
    products = models.ManyToManyField(
        "products.Product", null=True, blank=True, related_name="product"
    )

    def __str__(self):
        return f"{self.name}"
