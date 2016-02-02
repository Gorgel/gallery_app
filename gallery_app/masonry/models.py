import os
from django.db import models


def upload_path(self, filename):

    return os.path.join('paintings/', filename)

class Picture(models.Model):

    MASONRY_CLASSES = (
        ('grid-item', 'normal'),
        ('grid-item grid-item--width2', '2x width'),
        ('grid-item grid-item--width2--height2', '2x widht and height'),
        ('grid-item grid-item--height2', '2x height'),
          )
    PICTURE_TYPES = (
        ('water color', 'water color'),
        ('digital' , 'digital'),
    )

    picture_type = models.CharField(max_length=500, choices=PICTURE_TYPES)
    thumbnail = models.ImageField(upload_to=upload_path, blank=True)
    picture = models.ImageField(upload_to=upload_path, blank=True)
    masonry_class = models.CharField(max_length=100, choices=MASONRY_CLASSES)
    description = models.TextField(max_length=500)

    def __unicode__(self):
        return self.picture.url
#
# Create your models here.
