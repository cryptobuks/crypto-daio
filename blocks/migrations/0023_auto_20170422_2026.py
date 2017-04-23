# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0022_auto_20170422_2016'),
    ]

    operations = [
        migrations.RunSQL('SET CONSTRAINTS ALL IMMEDIATE',
                          reverse_sql=migrations.RunSQL.noop),
        migrations.AlterField(
            model_name='txinput',
            name='script_sig_asm',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='txinput',
            name='script_sig_hex',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.RunSQL(migrations.RunSQL.noop,
                          reverse_sql='SET CONSTRAINTS ALL IMMEDIATE'),
    ]
