# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='ready',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
