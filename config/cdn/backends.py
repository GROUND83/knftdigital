from storages.backends.s3boto3 import S3Boto3Storage
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = "static/"
    file_overwrite = False


class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = "media/"
