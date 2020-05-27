from django.db import migrations

def zoom_ratio_lensmodel(apps, schema_editor):
    lensmodel = apps.get_model('schema', 'LensModel')
    for row in lensmodel.objects.filter(zoom=True, min_focal_length__isnull=False, max_focal_length__isnull=False):
        row.zoom_ratio = row.max_focal_length / row.min_focal_length
        row.save()

def zoom_ratio_cameramodel(apps, schema_editor):
    cameramodel = apps.get_model('schema', 'CameraModel')
    for row in cameramodel.objects.filter(zoom=True, min_focal_length__isnull=False, max_focal_length__isnull=False):
        row.zoom_ratio = row.max_focal_length / row.min_focal_length
        row.save()

class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0060_auto_20200527_1946'),
    ]

    operations = [
        migrations.RunPython(zoom_ratio_lensmodel),
        migrations.RunPython(zoom_ratio_cameramodel),
    ]
