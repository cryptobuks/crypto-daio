# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0009_auto_20170622_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencyvalue',
            name='date_time',
            field=models.DateTimeField(auto_now=True, unique=True),
        ),
    ]
