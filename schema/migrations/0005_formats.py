from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    db_alias = schema_editor.connection.alias

    Format = apps.get_model("schema", "Format")
    Format.objects.using(db_alias).bulk_create([
        Format(format="120 roll"),
        Format(format="135 roll"),
        Format(format="620 roll"),
        Format(format="APS-C"),
        Format(format="Quarter plate"),
        Format(format="Polaroid 600"),
        Format(format="2.25x3.25\" sheet"),
        Format(format="6.5x9 sheet"),
        Format(format="4x5\" sheet"),
        Format(format="126 cartridge"),
        Format(format="110 cartridge"),
        Format(format="3¼x4\""),
        Format(format="116 roll"),
        Format(format="127 roll"),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0004_manufacturers'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
