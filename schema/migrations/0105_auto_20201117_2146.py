# Generated by Django 2.2.17 on 2020-11-17 21:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schema', '0104_delete_repair'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Enlarger',
            new_name='EnlargerModel',
        ),
    ]