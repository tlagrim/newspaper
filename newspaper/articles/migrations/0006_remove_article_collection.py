# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('articles', '0005_auto_20150223_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='collection',
        ),
    ]
