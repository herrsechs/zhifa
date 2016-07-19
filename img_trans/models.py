from django.db import models


# Create your models here.
class HairImg(models.Model):
    location = models.CharField(max_length=100)


class HeadImg(models.Model):
    location = models.CharField(max_length=100)


class SelfieImg(models.Model):
    location = models.CharField(max_length=100)



