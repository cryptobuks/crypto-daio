# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-25 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0023_usersocket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersocket',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
