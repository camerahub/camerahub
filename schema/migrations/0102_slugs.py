from __future__ import unicode_literals
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('schema', '0101_negative_slug'),
    ]
    operations = [
        migrations.RunPython(
            migrations.RunPython.noop, reverse_code=migrations.RunPython.noop),

    ]
