# Generated by Django 2.0 on 2018-03-05 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('variant', '0010_auto_20180305_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='indelmember',
            name='reference',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='variant.Reference'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snpmember',
            name='reference',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='variant.Reference'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='indelmember',
            unique_together={('reference', 'indel')},
        ),
        migrations.AlterUniqueTogether(
            name='snpmember',
            unique_together={('reference', 'snp')},
        ),
    ]
