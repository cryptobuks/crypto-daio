# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0024_auto_20170422_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='txinput',
            name='index',
            field=models.BigIntegerField(default=-1),
            preserve_default=False,
        ),
    ]
