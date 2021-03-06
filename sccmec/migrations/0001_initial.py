# Generated by Django 2.0 on 2017-12-13 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assembly', '0001_initial'),
        ('sample', '0001_initial'),
        ('staphopia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cassette',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('header', models.TextField()),
                ('length', models.PositiveIntegerField()),
                ('meca_start', models.PositiveIntegerField(default=0)),
                ('meca_stop', models.PositiveIntegerField(default=0)),
                ('meca_length', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Coverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=7)),
                ('minimum', models.PositiveIntegerField()),
                ('mean', models.DecimalField(decimal_places=2, max_digits=7)),
                ('median', models.PositiveIntegerField()),
                ('maximum', models.PositiveIntegerField()),
                ('meca_total', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('meca_minimum', models.PositiveIntegerField(default=0)),
                ('meca_mean', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('meca_median', models.PositiveIntegerField(default=0)),
                ('meca_maximum', models.PositiveIntegerField(default=0)),
                ('per_base_coverage', models.TextField()),
                ('cassette', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sccmec.Cassette')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.Sample')),
            ],
        ),
        migrations.CreateModel(
            name='Primers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bitscore', models.PositiveSmallIntegerField()),
                ('evalue', models.DecimalField(decimal_places=2, max_digits=7)),
                ('identity', models.PositiveSmallIntegerField()),
                ('mismatch', models.PositiveSmallIntegerField()),
                ('gaps', models.PositiveSmallIntegerField()),
                ('hamming_distance', models.PositiveSmallIntegerField()),
                ('query_from', models.PositiveSmallIntegerField()),
                ('query_to', models.PositiveSmallIntegerField()),
                ('hit_from', models.PositiveIntegerField()),
                ('hit_to', models.PositiveIntegerField()),
                ('align_len', models.PositiveSmallIntegerField()),
                ('qseq', models.TextField()),
                ('hseq', models.TextField()),
                ('midline', models.TextField()),
                ('contig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assembly.Contig')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staphopia.BlastQuery')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.Sample')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Proteins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bitscore', models.PositiveSmallIntegerField()),
                ('evalue', models.DecimalField(decimal_places=2, max_digits=7)),
                ('identity', models.PositiveSmallIntegerField()),
                ('mismatch', models.PositiveSmallIntegerField()),
                ('gaps', models.PositiveSmallIntegerField()),
                ('hamming_distance', models.PositiveSmallIntegerField()),
                ('query_from', models.PositiveSmallIntegerField()),
                ('query_to', models.PositiveSmallIntegerField()),
                ('hit_from', models.PositiveIntegerField()),
                ('hit_to', models.PositiveIntegerField()),
                ('align_len', models.PositiveSmallIntegerField()),
                ('qseq', models.TextField()),
                ('hseq', models.TextField()),
                ('midline', models.TextField()),
                ('contig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assembly.Contig')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staphopia.BlastQuery')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.Sample')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subtypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bitscore', models.PositiveSmallIntegerField()),
                ('evalue', models.DecimalField(decimal_places=2, max_digits=7)),
                ('identity', models.PositiveSmallIntegerField()),
                ('mismatch', models.PositiveSmallIntegerField()),
                ('gaps', models.PositiveSmallIntegerField()),
                ('hamming_distance', models.PositiveSmallIntegerField()),
                ('query_from', models.PositiveSmallIntegerField()),
                ('query_to', models.PositiveSmallIntegerField()),
                ('hit_from', models.PositiveIntegerField()),
                ('hit_to', models.PositiveIntegerField()),
                ('align_len', models.PositiveSmallIntegerField()),
                ('qseq', models.TextField()),
                ('hseq', models.TextField()),
                ('midline', models.TextField()),
                ('contig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assembly.Contig')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staphopia.BlastQuery')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.Sample')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='cassette',
            unique_together={('name', 'header')},
        ),
        migrations.AlterUniqueTogether(
            name='coverage',
            unique_together={('sample', 'cassette')},
        ),
    ]
