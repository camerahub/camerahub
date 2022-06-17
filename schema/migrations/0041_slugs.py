from __future__ import unicode_literals
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('schema', '0040_auto_20200321_2330'),
    ]
    operations = [
        migrations.RunPython(
            migrations.RunPython.noop, reverse_code=migrations.RunPython.noop),
    ]
