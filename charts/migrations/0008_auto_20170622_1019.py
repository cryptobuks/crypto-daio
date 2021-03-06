# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0007_currencyvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=26, null=True),
        ),
    ]
