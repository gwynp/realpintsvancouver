# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_location_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='alcohol',
        ),
        migrations.RemoveField(
            model_name='location',
            name='bathrooms',
        ),
        migrations.RemoveField(
            model_name='location',
            name='coffee',
        ),
        migrations.RemoveField(
            model_name='location',
            name='seating',
        ),
        migrations.AddField(
            model_name='location',
            name='selection',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Basic'), (2, b'Good'), (3, b'Really Good'), (4, b'Great')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='food',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Basic'), (2, b'Good'), (3, b'Really Good'), (4, b'Great')]),
        ),
    ]
