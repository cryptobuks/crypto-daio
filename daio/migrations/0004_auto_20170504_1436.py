# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-04 14:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daio', '0003_auto_20170504_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chain',
            old_name='rcp_user',
            new_name='rpc_user',
        ),
    ]