# Generated by Django 2.0.6 on 2018-09-28 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_aspirante_aceptado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='formacion',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='docente',
            name='titulo',
            field=models.CharField(max_length=20),
        ),
    ]
