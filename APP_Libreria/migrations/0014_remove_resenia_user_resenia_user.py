# Generated by Django 4.1 on 2022-10-10 00:59

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APP_Libreria', '0013_alter_resenia_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resenia',
            name='user',
        ),
        migrations.AddField(
            model_name='resenia',
            name='User',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]