# Generated by Django 4.0.3 on 2022-04-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_alter_works_iswc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='iswc',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
