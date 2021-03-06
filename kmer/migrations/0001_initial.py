# Generated by Django 2.0 on 2017-12-13 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sample', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField()),
                ('singletons', models.PositiveIntegerField()),
                ('sample', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sample.Sample')),
            ],
        ),
    ]
