from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0006_negative_sizes'),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop),
    ]
