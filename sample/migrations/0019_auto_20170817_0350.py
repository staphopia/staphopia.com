# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 03:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0018_auto_20170817_0323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metadata',
            old_name='city',
            new_name='region',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='state',
        ),
    ]
