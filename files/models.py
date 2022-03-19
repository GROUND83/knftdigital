from django.db import models
from core import models as core_models

# import magic
from django.utils.safestring import mark_safe

# from moviepy.editor import VideoFileClip
# from mimetypes import guess_type
# from .resize import resize_gif, resize_jpg, resize_viedo
import os.path
from config.settings import MEDIA_ROOT

# Create your models here.
class File(core_models.TimeStampedModel):

    """Photo Model Definition"""

    def get_file_path(self, filename):
        print(self.author)
        return os.path.join(
            self.author,
            filename,
        )

    def get_detail_file_path(self, filename):
        print(self.author)
        return os.path.join(
            self.author,
            filename,
        )

    class Meta:
        verbose_name = "파일"
        verbose_name_plural = "파일모음"

    author = models.CharField(max_length=80, verbose_name="작가이름", null=True, blank=True)
    caption = models.CharField(
        max_length=80, verbose_name="사진이름", null=True, blank=True
    )
    file = models.FileField(upload_to=get_file_path, null=True, blank=True)
    content_type = models.CharField(
        max_length=128, editable=True, null=True, blank=True
    )
    thumnail = models.FileField(upload_to=get_detail_file_path, null=True, blank=True)
    file360 = models.FileField(upload_to=get_detail_file_path, null=True, blank=True)
    file800 = models.FileField(upload_to=get_detail_file_path, null=True, blank=True)

    def __str__(self):
        return self.caption
