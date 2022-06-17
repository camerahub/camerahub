from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0079_auto_20200827_2049'),
    ]

    operations = [
        # omit reverse_code=... if you don't want the migration to be reversible.
        migrations.RunPython(migrations.RunPython.noop,
                             reverse_code=migrations.RunPython.noop),
    ]
