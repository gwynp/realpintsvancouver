# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20150902_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='pints',
        ),
        migrations.AddField(
            model_name='location',
            name='ontap',
            field=models.CharField(help_text='Fat Tug, Red Racer, Guinness, etc', max_length=300, null=True, blank=True),
        ),
    ]
