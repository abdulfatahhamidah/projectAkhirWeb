# Generated by Django 2.2 on 2021-01-12 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layanan', '0004_catalog_keyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='keyword',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='jenis_penulisan',
            field=models.CharField(choices=[('semua penulisan', 'Semua Penulisan'), ('disertasi', 'Disertasi'), ('tesis', 'Tesis'), ('skripsi', 'Skripsi')], default='semua penulisan', max_length=200),
        ),
        migrations.AlterField(
            model_name='repository',
            name='lokasi',
            field=models.CharField(choices=[('semua fakultas', 'Semua Fakultas'), ('ekonomi bisnis', 'Ekonomi dan Bisnis'), ('teknik', 'Teknik'), ('agama islam', 'Agama Islam'), ('psikologi', 'Psikologi'), ('kedokteran', 'Kedokteran'), ('keguruan', 'Keguruan dan Ilmu Pendidikan'), ('ilmu kesehatan', 'Ilmu Ilmu Kesehatan'), ('farmasi', 'Farmasi dan Sains'), ('sosial politik', 'Ilmu Sosial dan Ilmu Politik'), ('pascasarjana', 'Pascasarjana')], default='semua fakultas', max_length=200),
        ),
    ]
