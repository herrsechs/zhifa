from django.db import models


# Create your models here.
class HairImg(models.Model):
    bid = models.CharField(max_length=20)
    img = models.FileField(upload_to='/home/clouddata/img/haircut/', default=None)
    favor_count = models.IntegerField(default=0)


class HeadImg(models.Model):
    location = models.CharField(max_length=100)


class SelfieImg(models.Model):
    location = models.CharField(max_length=100)



