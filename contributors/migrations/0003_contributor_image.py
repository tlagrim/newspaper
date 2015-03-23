# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0002_auto_20150303_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='image',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
    ]
