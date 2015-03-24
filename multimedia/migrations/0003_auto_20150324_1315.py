# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0002_auto_20150324_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='section',
            field=models.ForeignKey(null=True, blank=True, to='sections.Section'),
            preserve_default=True,
        ),
    ]
