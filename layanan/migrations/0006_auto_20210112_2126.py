# Generated by Django 2.2 on 2021-01-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layanan', '0005_auto_20210112_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='bahasa',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='catalog',
            name='kepengarangan',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
