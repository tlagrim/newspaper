# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
  dependencies = [
    ('articles', '0004_auto_20150223_1717'),
  ]

  operations = [
    migrations.AlterField(
      model_name='article',
      name='content',
      field=models.TextField(),
      preserve_default=True,
    ),
  ]
