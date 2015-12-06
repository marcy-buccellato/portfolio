# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('difference', '0002_auto_20151202_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='difference',
            name='id',
        ),
        migrations.AlterField(
            model_name='difference',
            name='number',
            field=models.IntegerField(default=0, serialize=False, primary_key=True),
        ),
    ]
