# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Difference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=0)),
                ('value', models.IntegerField(default=0)),
                ('occurrences', models.IntegerField(default=0)),
                ('date', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
    ]
