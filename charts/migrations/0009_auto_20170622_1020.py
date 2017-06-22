# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0008_auto_20170622_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='base_amount',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='balance',
            name='quote_amount',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=26, null=True),
        ),
    ]