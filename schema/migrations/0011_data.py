from django.db import migrations

def forwards_func(apps, schema_editor):
  # We get the model from the versioned app registry;
  # if we directly import it, it'll be the wrong version
  db_alias = schema_editor.connection.alias

  Format = apps.get_model("schema", "Format")
  Format.objects.using(db_alias).bulk_create([
    Format(format="120 roll", digital="0"),
    Format(format="135 roll", digital="0"),
    Format(format="620 roll", digital="0"),
    Format(format="APS-C", digital="1"),
    Format(format="1/1.6\"", digital="1"),
    Format(format="Super 8mm", digital="0"),
    Format(format="8mm", digital="0"),
    Format(format="Quarter plate", digital="0"),
    Format(format="Polaroid 600", digital="0"),
    Format(format="2.25x3.25\" sheet", digital="0"),
    Format(format="6.5x9 sheet", digital="0"),
    Format(format="4x5\" sheet", digital="0"),
    Format(format="126 cartridge", digital="0"),
    Format(format="16mm", digital="0"),
    Format(format="110 cartridge", digital="0"),
    Format(format="3¼x4\"", digital="0"),
    Format(format="116 roll", digital="0"),
    Format(format="127 roll", digital="0"),
  ])
    

def reverse_func(apps, schema_editor):
  db_alias = schema_editor.connection.alias

  Format = apps.get_model("schema", "Format")
  Format.objects.using(db_alias).filter(format="120 roll")
  Format.objects.using(db_alias).filter(format="135 roll")
  Format.objects.using(db_alias).filter(format="620 roll")
  Format.objects.using(db_alias).filter(format="APS-C")
  Format.objects.using(db_alias).filter(format="1/1.6\"")
  Format.objects.using(db_alias).filter(format="Super 8mm")
  Format.objects.using(db_alias).filter(format="8mm")
  Format.objects.using(db_alias).filter(format="Quarter plate")
  Format.objects.using(db_alias).filter(format="Polaroid 600")
  Format.objects.using(db_alias).filter(format="2.25x3.25\" sheet")
  Format.objects.using(db_alias).filter(format="6.5x9 sheet")
  Format.objects.using(db_alias).filter(format="4x5\" sheet")
  Format.objects.using(db_alias).filter(format="126 cartridge")
  Format.objects.using(db_alias).filter(format="16mm")
  Format.objects.using(db_alias).filter(format="110 cartridge")
  Format.objects.using(db_alias).filter(format="3¼x4\"")
  Format.objects.using(db_alias).filter(format="116 roll")
  Format.objects.using(db_alias).filter(format="127 roll")
  


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0010_data'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
