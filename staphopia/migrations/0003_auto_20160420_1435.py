# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staphopia', '0002_auto_20160420_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blastquery',
            name='title',
            field=models.TextField(),
        ),
    ]
