# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default=0, upload_to='photos/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='categories',
            field=models.ManyToManyField(to='sections.Category', blank=True),
            preserve_default=True,
        ),
    ]
