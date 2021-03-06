# Generated by Django 2.0 on 2017-12-13 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sample', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.TextField(unique=True)),
                ('authors', models.TextField()),
                ('title', models.TextField()),
                ('abstract', models.TextField(db_index=True)),
                ('reference_ids', models.TextField()),
                ('keywords', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ToSample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publication.Publication')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publication_sample', to='sample.Sample')),
            ],
        ),
    ]
