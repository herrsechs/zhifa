# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customer_followed_barbers'),
        ('img_trans', '0002_auto_20160719_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=20)),
                ('cid', models.ForeignKey(to='account.Customer')),
                ('img_id', models.ForeignKey(to='img_trans.HairImg')),
            ],
        ),
    ]
