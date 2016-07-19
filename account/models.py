from django.db import models
from img_trans import models as img_models


genders = (
    ('m', 'male'),
    ('f', 'female'),
)


# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=genders)
    hairImgs = models.ManyToManyField(img_models.HairImg)
    selfieImgs = models.ManyToManyField(img_models.SelfieImg)
    headImgs = models.ManyToManyField(img_models.HeadImg)


class Barber(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=genders)
    hairImgs = models.ManyToManyField(img_models.HairImg)
    headImgs = models.ManyToManyField(img_models.HeadImg)
