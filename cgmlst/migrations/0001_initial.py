# Generated by Django 2.0 on 2018-01-31 18:14

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sample', '0003_auto_20171215_2005'),
        ('version', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CGMLST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentalist', django.contrib.postgres.fields.jsonb.JSONField()),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cgmlst_sample', to='sample.Sample')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cgmlst_version', to='version.Version')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentalist', models.TextField()),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cgmlst_report_sample', to='sample.Sample')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cgmlst_report_version', to='version.Version')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='report',
            unique_together={('sample', 'version')},
        ),
        migrations.AlterUniqueTogether(
            name='cgmlst',
            unique_together={('sample', 'version')},
        ),
    ]
