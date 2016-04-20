# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_metadata_md5sum'),
        ('sccmec', '0002_perbasecoverage'),
    ]

    operations = [
        migrations.AddField(
            model_name='perbasecoverage',
            name='sample',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sample.MetaData'),
            preserve_default=False,
        ),
    ]
