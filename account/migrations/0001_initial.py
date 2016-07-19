# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('img_trans', '0002_auto_20160719_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=1, choices=[(b'm', b'male'), (b'f', b'female')])),
                ('hairImgs', models.ManyToManyField(to='img_trans.HairImg')),
                ('headImgs', models.ManyToManyField(to='img_trans.HeadImg')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=1, choices=[(b'm', b'male'), (b'f', b'female')])),
                ('hairImgs', models.ManyToManyField(to='img_trans.HairImg')),
                ('headImgs', models.ManyToManyField(to='img_trans.HeadImg')),
                ('selfieImgs', models.ManyToManyField(to='img_trans.SelfieImg')),
            ],
        ),
    ]
