# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_type_plural'),
        ('shopping', '0003_saleerror'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(to='products.Product')),
                ('sale', models.ForeignKey(to='shopping.Sale')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='productsale',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productsale',
            name='sale',
        ),
        migrations.DeleteModel(
            name='ProductSale',
        ),
        migrations.AlterField(
            model_name='saleerror',
            name='message',
            field=models.CharField(max_length='500'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saleerror',
            name='problem',
            field=models.CharField(max_length='500'),
            preserve_default=True,
        ),
    ]
