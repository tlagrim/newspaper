# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('contributors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='description',
            field=models.CharField(max_length=200, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contributor',
            name='suffix',
            field=models.CharField(max_length=5, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contributor',
            name='class_standing',
            field=models.CharField(max_length=2,
                                   choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'),
                                            ('GR', 'Graduate')], blank=True),
            preserve_default=True,
        ),
    ]
