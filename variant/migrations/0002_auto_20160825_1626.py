# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-25 16:26
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('variant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='toindel',
            name='confidence',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tosnp',
            name='confidence',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
            preserve_default=False,
        ),
    ]