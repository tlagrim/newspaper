# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0003_contributor_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='position',
            field=models.CharField(choices=[('N/A', 'N/A'), ('peic', 'Print Editor-in-Chief'), ('oeic', 'Online Editor-in-Chief'), ('news', 'News Editor'), ('view', 'Viewpoints Editor'), ('life', 'Life & Arts Editor'), ('sports', 'Sports Editor'), ('dc', 'Design Chief'), ('d', 'Designer'), ('ope', 'Online Photo Editor'), ('pe', 'Photo Editor'), ('cc', 'Copy Chief'), ('ce', 'Copy Editor'), ('abm', 'Advertising & Business Manager'), ('w', 'writer'), ('p', 'photographer'), ('fa', 'Faculty Adviser')], default='N/A', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contributor',
            name='class_standing',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], blank=True, max_length=5),
            preserve_default=True,
        ),
    ]
