# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('slug', models.SlugField(unique=True, blank=True, editable=False)),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=1024)),
                ('type', models.CharField(choices=[('MIX', 'Dip Mix'), ('RUB', 'Dry Rub'), ('MAR', 'Marinade')], max_length='3')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('contains', models.ManyToManyField(to='products.Ingredient', null=True, blank=True)),
                ('perks', models.ManyToManyField(to='products.Perk', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
