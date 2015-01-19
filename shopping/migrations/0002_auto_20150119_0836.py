# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='live',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sale',
            name='status',
            field=models.CharField(default='O', choices=[('O', 'Ordered'), ('S', 'Sent')], max_length=1),
            preserve_default=True,
        ),
    ]
