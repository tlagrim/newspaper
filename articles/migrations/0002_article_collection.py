# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0003_remove_collection_categories'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='collection',
            field=models.ForeignKey(default=0, to='sections.Collection', blank=True),
            preserve_default=False,
        ),
    ]
