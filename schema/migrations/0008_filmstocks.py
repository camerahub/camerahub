from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0007_mounts'),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop),
    ]
