from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0069_auto_20200810_1812'),
    ]

    operations = [
        # omit reverse_code=... if you don't want the migration to be reversible.
        migrations.RunPython(migrations.RunPython.noop,
                             reverse_code=migrations.RunPython.noop),
    ]
