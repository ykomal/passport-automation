# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-23 16:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0005_auto_20181123_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dates',
            name='from_date',
            field=models.DateField(default=datetime.datetime(2018, 11, 23, 21, 49, 34, 491497)),
        ),
        migrations.AlterField(
            model_name='dates',
            name='to_date',
            field=models.DateField(default=datetime.datetime(2018, 11, 23, 21, 49, 34, 491497)),
        ),
    ]