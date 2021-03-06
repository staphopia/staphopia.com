# Generated by Django 2.0 on 2018-01-31 16:35

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('version', '0001_initial'),
        ('sample', '0003_auto_20171215_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ariba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('results', django.contrib.postgres.fields.jsonb.JSONField()),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='virulence_ariba_sample', to='sample.Sample')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='virulence_ariba_version', to='version.Version')),
            ],
        ),
        migrations.CreateModel(
            name='AribaSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequences', django.contrib.postgres.fields.jsonb.JSONField()),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='virulence_aribaseq_sample', to='sample.Sample')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='virulence_aribaseq_version', to='version.Version')),
            ],
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('ref_name', models.TextField()),
                ('original_name', models.TextField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='aribasequence',
            unique_together={('sample', 'version')},
        ),
        migrations.AlterUniqueTogether(
            name='ariba',
            unique_together={('sample', 'version')},
        ),
    ]
