# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0002_auto_20150303_1222'),
        ('articles', '0006_remove_article_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='second_author',
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(to='contributors.Contributor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='preview',
            field=models.CharField(max_length=200, default=0),
            preserve_default=False,
        ),
    ]
