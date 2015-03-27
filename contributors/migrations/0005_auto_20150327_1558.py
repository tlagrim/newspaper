# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0004_auto_20150327_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='staff',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contributor',
            name='position',
            field=models.CharField(default='N/A', max_length=10, choices=[('N/A', 'N/A'), ('peic', 'Print Editor-in-Chief'), ('oeic', 'Online Editor-in-Chief'), ('news', 'News Editor'), ('view', 'Viewpoints Editor'), ('life', 'Life & Arts Editor'), ('sports', 'Sports Editor'), ('dc', 'Design Chief'), ('d', 'Designer'), ('ope', 'Online Photo Editor'), ('pe', 'Photo Editor'), ('cc', 'Copy Chief'), ('ce', 'Copy Editor'), ('abm', 'Advertising & Business Manager'), ('w', 'writer'), ('p', 'photographer'), ('pro', 'programmer'), ('fa', 'Faculty Adviser')]),
            preserve_default=True,
        ),
    ]
