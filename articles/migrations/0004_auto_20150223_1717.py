# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
  dependencies = [
    ('articles', '0003_remove_article_article_style'),
  ]

  operations = [
    migrations.AlterField(
      model_name='article',
      name='collection',
      field=models.ForeignKey(blank=True, null=True, to='sections.Collection'),
      preserve_default=True,
    ),
    migrations.AlterField(
      model_name='article',
      name='second_author',
      field=models.ForeignKey(blank=True, null=True, to='contributors.Contributor'),
      preserve_default=True,
    ),
  ]
