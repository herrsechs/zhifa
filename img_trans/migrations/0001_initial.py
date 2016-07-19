# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=1, choices=[(b'm', b'male'), (b'f', b'female')])),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=1, choices=[(b'm', b'male'), (b'f', b'female')])),
            ],
        ),
        migrations.CreateModel(
            name='HairImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HeadImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SelfieImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='hairImgs',
            field=models.ManyToManyField(to='img_trans.HairImg'),
        ),
        migrations.AddField(
            model_name='customer',
            name='headImgs',
            field=models.ManyToManyField(to='img_trans.HeadImg'),
        ),
        migrations.AddField(
            model_name='customer',
            name='selfieImgs',
            field=models.ManyToManyField(to='img_trans.SelfieImg'),
        ),
        migrations.AddField(
            model_name='barber',
            name='hairImgs',
            field=models.ManyToManyField(to='img_trans.HairImg'),
        ),
        migrations.AddField(
            model_name='barber',
            name='headImgs',
            field=models.ManyToManyField(to='img_trans.HeadImg'),
        ),
    ]
