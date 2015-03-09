# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
  dependencies = [
    ('sections', '0007_auto_20150224_1205'),
  ]

  operations = [
    migrations.RemoveField(
      model_name='category',
      name='display',
    ),
    migrations.RemoveField(
      model_name='section',
      name='editor',
    ),
  ]
