# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fullcalendar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarevent',
            name='description',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calendarevent',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
            preserve_default=True,
        ),
    ]
