# Generated by Django 2.0 on 2017-12-07 19:18

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locus_tag', models.CharField(max_length=24)),
                ('protein_id', models.CharField(default='not_applicable', max_length=24)),
                ('gene', models.CharField(max_length=12)),
                ('product', models.TextField()),
                ('note', models.TextField()),
                ('is_pseudo', models.PositiveSmallIntegerField()),
                ('strand', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(db_index=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Counts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snp', models.PositiveIntegerField(default=0)),
                ('indel', models.PositiveIntegerField(default=0)),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.Sample')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_index=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Indel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_position', models.PositiveIntegerField(db_index=True)),
                ('reference_base', models.TextField()),
                ('alternate_base', models.TextField()),
                ('is_deletion', models.BooleanField(db_index=True, default=False)),
                ('annotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variant.Annotation')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variant.Feature')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_index=True, unique=True)),
                ('length', models.PositiveIntegerField(default=0)),
                ('sequence', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='ReferenceGenome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(default=0)),
                ('base', models.CharField(max_length=1)),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variant.Reference')),
            ],
        ),
        migrations.CreateModel(
            name='SNP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_position', models.PositiveIntegerField(db_index=True)),
                ('reference_base', models.CharField(max_length=1)),
                ('alternate_base', models.CharField(max_length=1)),
                ('reference_codon', models.CharField(max_length=3)),
                ('alternate_codon', models.CharField(max_length=3)),
                ('reference_amino_acid', models.CharField(max_length=1)),
                ('alternate_amino_acid', models.CharField(max_length=1)),
                ('codon_position', models.PositiveIntegerField()),
                ('snp_codon_position', models.PositiveSmallIntegerField()),
                ('amino_acid_change', models.TextField()),
                ('is_synonymous', models.PositiveSmallIntegerField()),
                ('is_transition', models.PositiveSmallIntegerField()),
                ('is_genic', models.PositiveSmallIntegerField()),
                ('annotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variant.Annotation')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variant.Feature')),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variant.Reference')),
            ],
        ),
        migrations.CreateModel(
            name='SNPCounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(db_index=True, default=0)),
                ('snp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variant.SNP')),
            ],
        ),
        migrations.CreateModel(
            name='ToIndel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confidence', django.contrib.postgres.fields.jsonb.JSONField()),
                ('filters', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variant.Filter')),
                ('indel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variant.Indel')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.Sample')),
            ],
        ),
        migrations.CreateModel(
            name='ToSNP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confidence', django.contrib.postgres.fields.jsonb.JSONField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variant.Comment')),
                ('filters', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variant.Filter')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.Sample')),
                ('snp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variant.SNP')),
            ],
        ),
        migrations.AddField(
            model_name='indel',
            name='reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variant.Reference'),
        ),
        migrations.AddField(
            model_name='feature',
            name='reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variant.Reference'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variant.Reference'),
        ),
        migrations.AlterUniqueTogether(
            name='tosnp',
            unique_together={('sample', 'snp')},
        ),
        migrations.AlterUniqueTogether(
            name='toindel',
            unique_together={('sample', 'indel')},
        ),
        migrations.AlterUniqueTogether(
            name='snp',
            unique_together={('reference', 'reference_position', 'reference_base', 'alternate_base')},
        ),
        migrations.AlterUniqueTogether(
            name='referencegenome',
            unique_together={('reference', 'position', 'base')},
        ),
        migrations.AlterUniqueTogether(
            name='indel',
            unique_together={('reference', 'reference_position', 'reference_base', 'alternate_base')},
        ),
    ]
