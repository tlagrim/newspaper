# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('articles', '0002_article_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_style',
        ),
    ]
