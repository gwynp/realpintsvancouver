# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150818_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='pints',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Pints'), (1, b'Pints and Sleeves')]),
        ),
    ]
