from __future__ import unicode_literals
from django.db import migrations, models
from slugify import UniqueSlugify


def addCustom(apps, schema_editor):

    ExistingRecords = apps.get_model('schema', 'cameramodel')

    custom_slugify_unique = UniqueSlugify(to_lower=True)

    for record in ExistingRecords.objects.all():
        record.slug = custom_slugify_unique("{} {} {}".format(
            record.manufacturer.name, record.model, str(record.disambiguation or '')))
        record.save()


class Migration(migrations.Migration):
    dependencies = [
        ('schema', '0035_cameramodel_slug'),
    ]
    operations = [
        migrations.RunPython(
            addCustom, reverse_code=migrations.RunPython.noop),
    ]
