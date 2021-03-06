# Generated by Django 4.0.3 on 2022-04-04 14:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('iswc', models.CharField(max_length=15, unique=True)),
                ('contributors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), blank=True, size=None)),
            ],
        ),
    ]
