# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_type_plural'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, upload_to='', null=True),
            preserve_default=True,
        ),
    ]
