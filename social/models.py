from django.db import models
# Create your models here.


class Comment(models.Model):
    text = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    cid = models.ForeignKey("account.Customer")
    img_id = models.ForeignKey("img_trans.HairImg")
