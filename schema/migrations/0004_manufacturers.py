from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0003_shutter_speeds')
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop),
    ]
