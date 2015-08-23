# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150818_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='outlets',
        ),
        migrations.AddField(
            model_name='location',
            name='neighbourhood',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='pints',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Just Pints'), (2, b'Pints and Sleeves')]),
        ),
    ]
