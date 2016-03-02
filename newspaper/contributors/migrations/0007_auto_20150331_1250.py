# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0006_auto_20150331_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='position',
            field=models.ForeignKey(default=0, to='contributors.Position'),
            preserve_default=False,
        ),
    ]
