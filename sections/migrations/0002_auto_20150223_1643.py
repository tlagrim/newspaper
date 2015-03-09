# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
  dependencies = [
    ('sections', '0001_initial'),
  ]

  operations = [
    migrations.CreateModel(
      name='Collection',
      fields=[
        ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
        ('name', models.CharField(max_length=20)),
        ('url', models.SlugField()),
        ('is_active', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
        ('categories', models.ManyToManyField(to='sections.Category')),
        ('section', models.ForeignKey(to='sections.Section')),
      ],
      options={
      },
      bases=(models.Model,),
    ),
    migrations.AlterField(
      model_name='section',
      name='name',
      field=models.CharField(max_length=20),
      preserve_default=True,
    ),
  ]
