# Generated by Django 2.2 on 2021-01-12 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('layanan', '0006_auto_20210112_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='kepengarangan',
        ),
    ]
