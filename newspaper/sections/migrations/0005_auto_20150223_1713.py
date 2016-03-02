# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('sections', '0004_remove_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='section',
            field=models.ForeignKey(to='sections.Section', null=True),
            preserve_default=True,
        ),
    ]
