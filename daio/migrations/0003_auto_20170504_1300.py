# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-04 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daio', '0002_auto_20170504_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chain',
            name='rpc_host',
            field=models.GenericIPAddressField(default='192.168.0.1'),
        ),
    ]