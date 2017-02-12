from django.db import models
# Create your models here.


class Comment(models.Model):
    text = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    cid = models.CharField(max_length=20)
    img_id = models.CharField(max_length=20)


class Message(models.Model):
    text = models.CharField(max_length=200)
    bid = models.CharField(max_length=20)
