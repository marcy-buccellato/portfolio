# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('difference', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='difference',
            name='date',
        ),
        migrations.AddField(
            model_name='difference',
            name='update_dt',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 2, 13, 21, 59, 457967, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
