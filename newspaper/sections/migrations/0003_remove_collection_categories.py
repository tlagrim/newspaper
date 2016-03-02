# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('sections', '0002_auto_20150223_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='categories',
        ),
    ]
