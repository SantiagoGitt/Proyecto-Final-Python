# Generated by Django 4.1 on 2022-10-10 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Libreria', '0019_resenia_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resenia',
            name='user',
        ),
    ]