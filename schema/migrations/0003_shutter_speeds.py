from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0002_data'),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop),
    ]
