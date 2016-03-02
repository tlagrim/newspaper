# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0007_auto_20150331_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='description',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='image',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='suffix',
            field=models.CharField(max_length=5, blank=True),
        ),
    ]
