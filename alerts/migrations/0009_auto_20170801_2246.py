# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0008_auto_20170801_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
