# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20150114_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='plural',
            field=models.CharField(default='none', max_length=20),
            preserve_default=False,
        ),
    ]
