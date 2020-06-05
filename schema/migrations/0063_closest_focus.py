from django.db import migrations

def closest_focus_lensmodel(apps, schema_editor):
    lensmodel = apps.get_model('schema', 'LensModel')
    for row in lensmodel.objects.filter(closest_focus__isnull=False):
        row.closest_focus = row.closest_focus / 100
        row.save()

def closest_focus_cameramodel(apps, schema_editor):
    cameramodel = apps.get_model('schema', 'CameraModel')
    for row in cameramodel.objects.filter(closest_focus__isnull=False):
        row.closest_focus = row.closest_focus / 100
        row.save()

class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0062_auto_20200529_2059'),
    ]

    operations = [
        migrations.RunPython(closest_focus_lensmodel),
        migrations.RunPython(closest_focus_cameramodel),
    ]
