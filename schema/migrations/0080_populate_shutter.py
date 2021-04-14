from django.db import migrations
from django.db.models import Max, Min


def populate_shutter_speeds(apps, schema_editor):
    cameramodel = apps.get_model('schema', 'CameraModel')

    for row in cameramodel.objects.all():
        if row.fastest_shutter_speed is None:
            row.fastest_shutter_speed = row.shutter_speeds.order_by(
                'duration').first()
        if row.slowest_shutter_speed is None:
            row.slowest_shutter_speed = row.shutter_speeds.order_by(
                '-duration').first()
        row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0079_auto_20200827_2049'),
    ]

    operations = [
        # omit reverse_code=... if you don't want the migration to be reversible.
        migrations.RunPython(populate_shutter_speeds,
                             reverse_code=migrations.RunPython.noop),
    ]
