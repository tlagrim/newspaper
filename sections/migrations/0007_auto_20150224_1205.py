# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
  dependencies = [
    ('sections', '0006_auto_20150223_1715'),
  ]

  operations = [
    migrations.RemoveField(
      model_name='collection',
      name='section',
    ),
    migrations.DeleteModel(
      name='Collection',
    ),
    migrations.AddField(
      model_name='category',
      name='display',
      field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, default='N'),
      preserve_default=True,
    ),
  ]
