# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
  dependencies = [
    ('contributors', '0001_initial'),
    ('sections', '__first__'),
  ]

  operations = [
    migrations.CreateModel(
      name='Article',
      fields=[
        ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
        ('title', models.CharField(max_length=50)),
        ('url', models.SlugField()),
        ('content', models.TextField(max_length=200)),
        ('date_published', models.DateField()),
        ('article_style', models.CharField(max_length=2)),
        ('author', models.ForeignKey(related_name='+', to='contributors.Contributor')),
        ('categories', models.ManyToManyField(to='sections.Category', blank=True)),
        ('main_category', models.ForeignKey(related_name='+', to='sections.Category')),
        ('second_author', models.ForeignKey(to='contributors.Contributor', blank=True)),
        ('section', models.ForeignKey(to='sections.Section')),
      ],
      options={
      },
      bases=(models.Model,),
    ),
  ]
