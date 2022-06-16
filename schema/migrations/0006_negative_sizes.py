from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0005_formats'),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop),
    ]
