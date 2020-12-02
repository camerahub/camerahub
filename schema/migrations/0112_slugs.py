from __future__ import unicode_literals
from django.db import migrations, models


def addFlash(apps, schema_editor):
    flashes = apps.get_model('schema', 'flashmodel')
    for record in flashes.objects.all():
        record.save()


def addEnlarger(apps, schema_editor):
    enlargers = apps.get_model('schema', 'enlargermodel')
    for record in enlargers.objects.all():
        record.save()


def addTeleconverter(apps, schema_editor):
    teleconverters = apps.get_model('schema', 'teleconvertermodel')
    for record in teleconverters.objects.all():
        record.save()


class Migration(migrations.Migration):
    dependencies = [
        ('schema', '0111_auto_20201126_2251'),
    ]
    operations = [
        migrations.RunPython(
            addFlash, reverse_code=migrations.RunPython.noop
        ),
        migrations.RunPython(
            addEnlarger, reverse_code=migrations.RunPython.noop
        ),
        migrations.RunPython(
            addTeleconverter, reverse_code=migrations.RunPython.noop
        ),
    ]
