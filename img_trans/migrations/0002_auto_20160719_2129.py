# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('img_trans', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barber',
            name='hairImgs',
        ),
        migrations.RemoveField(
            model_name='barber',
            name='headImgs',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='hairImgs',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='headImgs',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='selfieImgs',
        ),
        migrations.DeleteModel(
            name='Barber',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
