from __future__ import unicode_literals
from django.db import migrations, models
from django.contrib.auth.models import User
import os


def forwards_func(apps, schema_editor):
    User.objects.create_superuser('admin', email=os.getenv(
        'CAMERAHUB_ADMIN_EMAIL', 'admin@example.com'), password=os.getenv('CAMERAHUB_ADMIN_PASSWORD', 'admin'))


def reverse_func(apps, schema_editor):
    # destroy what forward_func builds
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('schema', '0019_auto_20200110_1728_squashed_0020_auto_20200110_1734'),
    ]
    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
