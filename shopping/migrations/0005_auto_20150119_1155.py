# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_auto_20150119_1018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='saleproduct',
            name='price',
            field=models.DecimalField(max_digits=6, decimal_places=2, default=5.55),
            preserve_default=False,
        ),
    ]
