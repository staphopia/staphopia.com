# Generated by Django 2.0 on 2017-12-13 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('version', '0001_initial'),
        ('sample', '0002_md5'),
        ('assembly', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contig',
            name='version',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='assembly_contig_version', to='version.Version'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='summary',
            name='version',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='assembly_summary_version', to='version.Version'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='contig',
            unique_together={('sample', 'version', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='summary',
            unique_together={('sample', 'version')},
        ),
    ]
