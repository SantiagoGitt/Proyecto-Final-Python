# Generated by Django 4.1 on 2022-09-05 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Libreria', '0002_rename_cumpleanios_clientes_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='correo',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nacimiento',
            field=models.CharField(max_length=64),
        ),
    ]
