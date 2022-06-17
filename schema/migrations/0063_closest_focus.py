from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0062_auto_20200529_2059'),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop),
    ]
