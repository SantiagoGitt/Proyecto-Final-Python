# Generated by Django 4.1 on 2022-10-11 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Libreria', '0025_alter_avatar_user_alter_resenia_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='user',
        ),
        migrations.RemoveField(
            model_name='resenia',
            name='user',
        ),
    ]
