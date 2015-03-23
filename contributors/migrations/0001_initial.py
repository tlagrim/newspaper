# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('twitter', models.SlugField()),
                ('email', models.EmailField(max_length=75)),
                ('bio', models.TextField()),
                ('class_standing', models.CharField(default='NA', blank=True, max_length=2,
                                                    choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'),
                                                             ('SR', 'Senior'), ('GR', 'Graduate')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
