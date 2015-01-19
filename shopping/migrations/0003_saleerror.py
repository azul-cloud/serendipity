# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20150119_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleError',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('location', models.CharField(choices=[('C', 'Card'), ('A', 'Cart'), ('S', 'Sale'), ('I', 'Items')], max_length='1')),
                ('message', models.CharField(max_length='100')),
                ('problem', models.CharField(max_length='200')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
