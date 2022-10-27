from multiprocessing.dummy import Process
from django.db import models
from imagekit.processors import ResizeToFit, Thumbnail
from imagekit.models import ProcessedImageField

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    image = ProcessedImageField(
        blank=True,
        upload_to='thumbnails/',
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality': 80},
    )