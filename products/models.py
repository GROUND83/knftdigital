from django.db import models

from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Tag(AbstractItem):
    class Meta:
        verbose_name_plural = "Tags"


class ProjectType(AbstractItem):

    """RoomType Model Definition"""

    class Meta:
        verbose_name = "projectType"


class Type(AbstractItem):

    """RoomType Model Definition"""

    class Meta:
        verbose_name = "Type"


# Create your models here.
class Product(core_models.TimeStampedModel):
    class Meta:
        verbose_name = "작품"
        verbose_name_plural = "작품"
        ordering = ["title"]

    PRODUCT_TYPE_CHOICES = (
        ("project", "project"),
        ("edition", "edition"),
        ("other", "other"),
    )
    PROJECT_TYPE_CHOICES = (
        ("the Love", "the Love"),
        ("the Load", "the Load"),
    )
    TYPE_CHOICES = (
        ("Notable", "Notable"),
        ("Caligraphy", "Caligraphy"),
        ("Engraving", "Engraving"),
        ("Illustration", "Illustration"),
        ("Photography", "Photography"),
    )

    title = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="작품 타이틀", unique=False
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="작품 설명",
    )

    author = models.ForeignKey(
        "authors.Author", on_delete=models.CASCADE, related_name="author"
    )
    creationDate = models.DateField(null=True, blank=True)
    type = models.ForeignKey(
        "Type", related_name="products", on_delete=models.SET_NULL, null=True
    )
    dimensionsx = models.CharField(
        max_length=10, null=True, blank=True, verbose_name="x 사이즈", unique=False
    )
    dimensionsy = models.CharField(
        max_length=10, null=True, blank=True, verbose_name="y 사이즈", unique=False
    )
    product_type = models.CharField(
        choices=PRODUCT_TYPE_CHOICES,
        max_length=40,
        default="project",
        null=True,
        blank=True,
        verbose_name="product_type",
    )
    project_type = models.ForeignKey(
        "ProjectType", related_name="products", on_delete=models.SET_NULL, null=True
    )
    #
    projectTitle = models.CharField(
        max_length=100,
        null=True,
        verbose_name="project title",
        unique=False,
        blank=True,
    )
    edtionTitle = models.CharField(
        max_length=100,
        null=True,
        verbose_name="edtion title",
        unique=False,
        blank=True,
    )
    otherTitle = models.CharField(
        max_length=100,
        null=True,
        verbose_name="other title",
        unique=False,
        blank=True,
    )
    # 소셜
    foundataionLink = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="foundataionLink",
        unique=False,
    )
    openseaLink = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="openseaLink", unique=False
    )
    solahartLink = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="solahartLink", unique=False
    )
    raribleLink = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="raribleLink", unique=False
    )
    # 이미지
    image = models.ForeignKey(
        "files.File", on_delete=models.CASCADE, null=True, blank=True
    )

    main = models.BooleanField(default=False, verbose_name="메인작품")
    number = models.PositiveIntegerField(
        default=1, null=True, blank=True, verbose_name="작품넘버"
    )
    hit = models.PositiveIntegerField(
        default=0, null=True, blank=True, verbose_name="hit"
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="ETH 가격",
    )
    tags = models.ManyToManyField(Tag, null=True, blank=True, verbose_name="tag")
    theme = models.CharField(
        max_length=100, null=True, verbose_name="theme", unique=False
    )

    def __str__(self):
        return f"{self.title}"
