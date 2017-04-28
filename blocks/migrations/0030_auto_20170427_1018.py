# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0029_auto_20170426_0746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['index']},
        ),
        migrations.AlterModelOptions(
            name='txinput',
            options={'ordering': ['-index']},
        ),
        migrations.AlterModelOptions(
            name='txoutput',
            options={'ordering': ['-index']},
        ),
        migrations.AlterField(
            model_name='transaction',
            name='tx_id',
            field=models.CharField(max_length=610, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='txoutput',
            unique_together=set([('transaction', 'index')]),
        ),
    ]