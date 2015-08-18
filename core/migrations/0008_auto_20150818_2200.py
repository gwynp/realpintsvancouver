# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_location_pints'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='website',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
