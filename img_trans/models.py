from django.db import models


# Create your models here.
class HairImg(models.Model):
    barber = models.ForeignKey("account.Barber", on_delete=models.CASCADE)
    img = models.FileField(upload_to='/home/clouddata/img/'+barber+'/')
    favor_count = models.IntegerField()


class HeadImg(models.Model):
    location = models.CharField(max_length=100)


class SelfieImg(models.Model):
    location = models.CharField(max_length=100)



