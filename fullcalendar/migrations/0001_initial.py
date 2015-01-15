# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(blank=True, verbose_name='Title', max_length=200)),
                ('start', models.DateTimeField(verbose_name='Start')),
                ('end', models.DateTimeField(verbose_name='End')),
                ('all_day', models.BooleanField(verbose_name='All day', default=False)),
            ],
            options={
                'verbose_name_plural': 'Events',
                'verbose_name': 'Event',
            },
            bases=(models.Model,),
        ),
    ]
