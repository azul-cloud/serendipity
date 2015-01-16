# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fullcalendar', '0002_auto_20150115_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('fullcalendar.calendarevent',),
        ),
    ]
