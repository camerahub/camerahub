from __future__ import unicode_literals
from django.db import migrations, models
from django.contrib.auth.models import User     # where User lives
import os                                      # env var accessA

def forwards_func(apps, schema_editor):
    # build the user you now have access to via Django magic
    #User.objects.create_superuser('admin', os.getenv('ADMIN_PASSWORD')
    User.objects.create_superuser('admin', email='admin@example.com', password='admin')

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
