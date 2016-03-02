# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_article_ready'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='date_published',
            new_name='publish_date',
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name=''),
            preserve_default=True,
        ),
    ]
