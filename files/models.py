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
        return self.author

    # def save(self, *args, **kwargs):
    #     if os.path.isdir(os.path.join(MEDIA_ROOT, f"{self.author}/{self.caption}")):
    #         pass
    #     else:
    #         os.makedirs(
    #             os.path.join(MEDIA_ROOT, f"{self.author}/{self.caption}"),
    #             exist_ok=True,
    #         )
    #     mine = magic.from_buffer(self.file.read(), mime=True)
    #     self.content_type = mine
    #     print(mine)
    #     if mine == "image/jpeg" or mine == "image/png":
    #         print(self.file.name)
    #         thumnailName = resize_jpg(
    #             image=self.file, width=80, name=self.author, caption=self.caption
    #         )

    #         upladName360 = resize_jpg(
    #             image=self.file, width=360, name=self.author, caption=self.caption
    #         )
    #         upladName800 = resize_jpg(
    #             image=self.file, width=800, name=self.author, caption=self.caption
    #         )
    #         print(thumnailName)
    #         self.thumnail = thumnailName
    #         self.file360 = upladName360
    #         self.file800 = upladName800
    #     elif mine == "image/gif":
    #         thumnailName = resize_gif(
    #             image=self.file, width=80, name=self.author, caption=self.caption
    #         )
    #         upladName360 = resize_gif(
    #             image=self.file, width=360, name=self.author, caption=self.caption
    #         )
    #         upladName800 = resize_gif(
    #             image=self.file, width=800, name=self.author, caption=self.caption
    #         )
    #         self.thumnail = thumnailName
    #         self.file360 = upladName360
    #         self.file800 = upladName800

    #     elif mine == "video/mp4":
    #         # self.file.save()
    #         super().save(**kwargs)

    #         print(self.file.path)
    #         filename = self.file.name.split(".")
    #         upladName360 = (
    #             f"{self.author}/{self.caption}/360_{self.caption}.{filename[1]}"
    #         )
    #         upladName800 = (
    #             f"{self.author}/{self.caption}/800_{self.caption}.{filename[1]}"
    #         )
    #         imgupladName = f"{self.author}/{self.caption}/thum_{self.caption}.jpg"
    #         # self.avator 확인 동영상 ? 이미지? gif?
    #         clip = VideoFileClip(self.file.path)

    #         clip_resized360 = clip.resize(width=360)
    #         clip_resized800 = clip.resize(width=800)

    #         clip_resized360.write_videofile(
    #             os.path.join(
    #                 MEDIA_ROOT,
    #                 f"{self.author}/{self.caption}/360_{self.caption}.{filename[1]}",
    #             ),
    #         )
    #         clip_resized800.write_videofile(
    #             os.path.join(
    #                 MEDIA_ROOT,
    #                 f"{self.author}/{self.caption}/800_{self.caption}.{filename[1]}",
    #             )
    #         )
    #         # 프리뷰
    #         clip_resized360.save_frame(
    #             os.path.join(
    #                 MEDIA_ROOT, f"{self.author}/{self.caption}/thum_{self.caption}.jpg"
    #             ),
    #             t=1.00,
    #         )

    #         self.thumnail = imgupladName
    #         self.file360 = upladName360
    #         self.file800 = upladName800
    #         # self.save()
    #         print(clip_resized360)
    #     super().save(**kwargs)
