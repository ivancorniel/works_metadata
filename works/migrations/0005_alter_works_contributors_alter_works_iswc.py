# Generated by Django 4.0.3 on 2022-04-04 19:48

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0004_alter_works_contributors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='contributors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='works',
            name='iswc',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
