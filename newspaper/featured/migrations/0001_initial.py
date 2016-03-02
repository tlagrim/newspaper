# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0009_auto_20150920_2144'),
        ('articles', '0011_auto_20150920_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article', models.ForeignKey(related_name='+', to='articles.Article')),
                ('section', models.ForeignKey(to='sections.Section')),
            ],
        ),
        migrations.CreateModel(
            name='MainStory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
                ('article', models.ForeignKey(related_name='+', to='articles.Article')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name_plural': 'Main stories',
            },
        ),
        migrations.CreateModel(
            name='PinnedArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
                ('article', models.ForeignKey(related_name='+', to='articles.Article')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
