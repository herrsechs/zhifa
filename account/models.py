from django.db import models
from img_trans import models as img_models


genders = (
    ('m', 'male'),
    ('f', 'female'),
)


class Barber(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=genders)


# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=genders)
    followed_barbers = models.ManyToManyField(Barber)




