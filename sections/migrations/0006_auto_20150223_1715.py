# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
  dependencies = [
    ('sections', '0005_auto_20150223_1713'),
  ]

  operations = [
    migrations.AlterField(
      model_name='category',
      name='section',
      field=models.ForeignKey(to='sections.Section', blank=True, null=True),
      preserve_default=True,
    ),
  ]
