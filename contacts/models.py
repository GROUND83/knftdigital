from django.db import models
from core import models as core_models


class Contact(core_models.TimeStampedModel):
    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"

    CONTACT_TYPE_CHOICES = (
        ("collect", "collect"),
        ("contact", "contact"),
    )
    HELP_TYPE_CHOICES = (
        ("Buying NFTs", "Buying NFTs"),
        ("Question about NFT art", "Question about NFT art"),
        ("Participating in an NFT project", "Participating in an NFT project"),
        ("Question about K-NFT", "Question about K-NFT"),
        ("Partnering with K-NFT", "Partnering with K-NFT"),
        ("Other", "Other"),
    )
    type = models.CharField(
        choices=CONTACT_TYPE_CHOICES,
        max_length=200,
        null=True,
        blank=True,
        verbose_name="type",
        default="collect",
    )
    email = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="email", unique=False
    )
    name = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="name", unique=False
    )
    helpType = models.CharField(
        choices=HELP_TYPE_CHOICES,
        max_length=200,
        null=True,
        blank=True,
        verbose_name="helpType",
        unique=False,
        default="Buying NFTs",
    )
    message = models.TextField(
        max_length=200, null=True, blank=True, verbose_name="message", unique=False
    )

    def __str__(self):
        return self.email
