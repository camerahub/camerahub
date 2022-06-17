from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0060_auto_20200527_1946'),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop),
    ]
