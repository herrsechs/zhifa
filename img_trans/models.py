from django.db import models


# Create your models here.
class HairImg(models.Model):
    bid = models.CharField(max_length=20)
    img = models.FileField(upload_to='/home/clouddata/img/haircut/', default=None)
    favor_count = models.IntegerField(default=0)
    gender = models.CharField(max_length=45, default='female')
    type = models.CharField(max_length=45, default='short')


class HeadImg(models.Model):
    user_id = models.CharField(max_length=20)
    img = models.FileField(upload_to='/home/clouddata/img/headimg/', default=None)
    role = models.CharField(max_length=20)


class SelfieImg(models.Model):
    cid = models.CharField(max_length=20)
    img = models.FileField(upload_to='/home/clouddata/img/selfie', default=None)



