# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0031_auto_20170430_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='txinput',
            name='coin_base',
            field=models.CharField(blank=True, default='', max_length=610),
            preserve_default=False,
        ),
    ]