# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_auto_20150119_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleerror',
            name='sale',
            field=models.ForeignKey(null=True, to='shopping.Sale'),
            preserve_default=True,
        ),
    ]
