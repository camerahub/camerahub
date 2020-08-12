from django.db import migrations


def populate_metering_modes(apps, schema_editor):
    cameramodel = apps.get_model('schema', 'CameraModel')
    meteringmode = apps.get_model('schema', 'MeteringMode')
    nometering = meteringmode.objects.get(name='None')

    for row in cameramodel.objects.filter(metering=False):
        row.metering_modes.add(nometering)
        row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0069_auto_20200810_1812'),
    ]

    operations = [
        # omit reverse_code=... if you don't want the migration to be reversible.
        migrations.RunPython(populate_metering_modes,
                             reverse_code=migrations.RunPython.noop),
    ]
