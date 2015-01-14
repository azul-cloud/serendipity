# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(max_length=3, choices=[('MIX', 'Dip Mix'), ('RUB', 'Dry Rub'), ('MAR', 'Marinade')]),
            preserve_default=True,
        ),
    ]
