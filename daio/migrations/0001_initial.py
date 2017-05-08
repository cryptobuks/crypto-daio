# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-04 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tenant_schemas.postgresql_backend.base


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_url', models.CharField(max_length=128, unique=True)),
                ('schema_name', models.CharField(max_length=63, unique=True, validators=[tenant_schemas.postgresql_backend.base._check_schema_name])),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('unit_code', models.CharField(max_length=255)),
                ('chain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coins', related_query_name='coin', to='daio.Chain')),
            ],
        ),
    ]