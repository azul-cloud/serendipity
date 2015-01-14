# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='active',
            new_name='available',
        ),
    ]
