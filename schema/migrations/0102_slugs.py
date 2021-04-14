from __future__ import unicode_literals
from django.db import migrations, models


def addNegative(apps, schema_editor):
    negatives = apps.get_model('schema', 'negative')
    for record in negatives.objects.all():
        record.slug = str(record.film.id_owner) + ':' + str(record.frame)
        record.save()

class Migration(migrations.Migration):
    dependencies = [
        ('schema', '0101_negative_slug'),
    ]
    operations = [
        migrations.RunPython(
            addNegative, reverse_code=migrations.RunPython.noop),

    ]
