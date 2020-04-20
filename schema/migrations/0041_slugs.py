from __future__ import unicode_literals
from django.db import migrations, models
from slugify import UniqueSlugify


def addManufacturer(apps, schema_editor):
    ExistingRecords = apps.get_model('schema', 'manufacturer')
    custom_slugify_unique = UniqueSlugify(to_lower=True)
    for record in ExistingRecords.objects.all():
        record.slug = custom_slugify_unique(record.name)
        record.save()


def addBattery(apps, schema_editor):
    ExistingRecords = apps.get_model('schema', 'battery')
    custom_slugify_unique = UniqueSlugify(to_lower=True)
    for record in ExistingRecords.objects.all():
        record.slug = custom_slugify_unique(record.name)
        record.save()


def addMount(apps, schema_editor):
    ExistingRecords = apps.get_model('schema', 'mount')
    custom_slugify_unique = UniqueSlugify(to_lower=True)
    for record in ExistingRecords.objects.all():
        record.slug = custom_slugify_unique(record.mount)
        record.save()


def addToner(apps, schema_editor):
    ExistingRecords = apps.get_model('schema', 'toner')
    custom_slugify_unique = UniqueSlugify(to_lower=True)
    for record in ExistingRecords.objects.all():
        record.slug = custom_slugify_unique(
            "{} {}".format(record.manufacturer.name, record.name))
        record.save()


def addFilmstock(apps, schema_editor):
    ExistingRecords = apps.get_model('schema', 'filmstock')
    custom_slugify_unique = UniqueSlugify(to_lower=True)
    for record in ExistingRecords.objects.all():
        record.slug = custom_slugify_unique(
            "{} {}".format(record.manufacturer.name, record.name))
        record.save()


def addDeveloper(apps, schema_editor):
    ExistingRecords = apps.get_model('schema', 'developer')
    custom_slugify_unique = UniqueSlugify(to_lower=True)
    for record in ExistingRecords.objects.all():
        record.slug = custom_slugify_unique(
            "{} {}".format(record.manufacturer.name, record.name))
        record.save()


def addLensmodel(apps, schema_editor):
    ExistingRecords = apps.get_model('schema', 'lensmodel')
    custom_slugify_unique = UniqueSlugify(to_lower=True)
    for record in ExistingRecords.objects.all():
        record.slug = custom_slugify_unique("{} {} {}".format(
            record.manufacturer.name, record.model, str(record.disambiguation or '')))
        record.save()


class Migration(migrations.Migration):
    dependencies = [
        ('schema', '0040_auto_20200321_2330'),
    ]
    operations = [
        migrations.RunPython(
            addManufacturer, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(
            addBattery, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(addMount, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(addToner, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(
            addFilmstock, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(
            addDeveloper, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(
            addLensmodel, reverse_code=migrations.RunPython.noop),
    ]
