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
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_added', models.DateField()),
                ('categories', models.ManyToManyField(to='sections.Category')),
                ('photographer', models.ForeignKey(to='contributors.Contributor')),
                ('section', models.ForeignKey(blank=True, to='sections.Section')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
