from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0004_manufacturers'),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop),
    ]
