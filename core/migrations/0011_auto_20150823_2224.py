# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150823_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='image_file',
            field=models.ImageField(null=True, upload_to=b'media/photos', blank=True),
        ),
    ]
