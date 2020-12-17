from __future__ import unicode_literals
from django.db import migrations, models
from slugify import slugify


def addNegative(apps, schema_editor):
    negatives = apps.get_model('schema', 'negative')
    for record in negatives.objects.all():
        record.slug = slugify(str(record.film.id_owner) + '.' + str(record.frame), separator='.')
        record.save()

class Migration(migrations.Migration):
    dependencies = [
        ('schema', '0116_auto_20201216_2013'),
    ]
    operations = [
        migrations.RunPython(
            addNegative, reverse_code=migrations.RunPython.noop),

    ]
