from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    db_alias = schema_editor.connection.alias

    Mount = apps.get_model("schema", "Mount")
    Manufacturer = apps.get_model("schema", "Manufacturer")

    Manufacturer.objects.using(db_alias).bulk_create([
        Manufacturer(name="Alpa", country="Switzerland",
                     url="http://www.alpa.ch"),
        Manufacturer(name="Bronica", city="Tokyo",
                     country="Japan", founded="1956"),
        Manufacturer(name="Hasselblad", city="Gothenburg", country="Sweden",
                     url="https://www.hasselblad.com", founded="1841"),
        Manufacturer(name="Ihagee", city="Dresden",
                     country="Germany", founded="1912"),
        Manufacturer(name="Kowa", country="Japan", founded="1954"),
        Manufacturer(name="Petri", country="Japan", founded="1907"),
    ], ignore_conflicts=True)

    Alpa = Manufacturer.objects.get(name='Alpa')
    Mount.objects.using(db_alias).update_or_create(
        mount="Alpa", type='Bayonet', purpose='Camera', manufacturer=Alpa)

    Braun = Manufacturer.objects.get(name='Braun')
    Mount.objects.using(db_alias).update_or_create(
        mount="Paxette", shutter_in_lens=0, type='Screw', purpose='Camera', manufacturer=Braun)

    Bronica = Manufacturer.objects.get(name='Bronica')
    Mount.objects.using(db_alias).update_or_create(
        mount="Bronica ETR", type='Bayonet', purpose='Camera', manufacturer=Bronica)
    Mount.objects.using(db_alias).update_or_create(
        mount="Bronica GS1", type='Bayonet', purpose='Camera', manufacturer=Bronica)
    Mount.objects.using(db_alias).update_or_create(
        mount="Bronica RF", type='Bayonet', purpose='Camera', manufacturer=Bronica)
    Mount.objects.using(db_alias).update_or_create(
        mount="Bronica SQA", type='Bayonet', purpose='Camera', manufacturer=Bronica)

    Canon = Manufacturer.objects.get(name='Canon')
    Mount.objects.using(db_alias).update_or_create(
        mount="Canon EF", shutter_in_lens=0, type='Bayonet', purpose='Camera', manufacturer=Canon)
    Mount.objects.using(db_alias).update_or_create(
        mount="Canon EF-M", shutter_in_lens=0, type='Bayonet', purpose='Camera', manufacturer=Canon)
    Mount.objects.using(db_alias).update_or_create(
        mount="Canon EF-S", shutter_in_lens=0, type='Bayonet', purpose='Camera', manufacturer=Canon)
    Mount.objects.using(db_alias).update_or_create(
        mount="Canon EX", shutter_in_lens=0, type='Bayonet', purpose='Camera', manufacturer=Canon)
    Mount.objects.using(db_alias).update_or_create(
        mount="Canon FD", shutter_in_lens=0, type='Breech lock', purpose='Camera', manufacturer=Canon)
    Mount.objects.using(db_alias).update_or_create(
        mount="Canon FL", shutter_in_lens=0, type='Breech lock', purpose='Camera', manufacturer=Canon)

    Fuji = Manufacturer.objects.get(name='Fuji')
    Mount.objects.using(db_alias).update_or_create(
        mount="Fujica X", type='Bayonet', purpose='Camera', manufacturer=Fuji)

    Hasselblad = Manufacturer.objects.get(name='Hasselblad')
    Mount.objects.using(db_alias).update_or_create(
        mount="Hasselblad", type='Bayonet', purpose='Camera', manufacturer=Hasselblad)
    Mount.objects.using(db_alias).update_or_create(
        mount="Hasselblad Xpan", type='Bayonet', purpose='Camera', manufacturer=Hasselblad)

    Ihagee = Manufacturer.objects.get(name='Ihagee')
    Mount.objects.using(db_alias).update_or_create(
        mount="Exakta", type='Bayonet', purpose='Camera', manufacturer=Ihagee)

    Konica = Manufacturer.objects.get(name='Konica')
    Mount.objects.using(db_alias).update_or_create(
        mount="KM", type='Bayonet', purpose='Camera', manufacturer=Konica)
    Mount.objects.using(db_alias).update_or_create(
        mount="Konica AR", type='Bayonet', purpose='Camera', manufacturer=Konica)
    Mount.objects.using(db_alias).update_or_create(
        mount="Konica F", type='Bayonet', purpose='Camera', manufacturer=Konica)

    Kowa = Manufacturer.objects.get(name='Kowa')
    Mount.objects.using(db_alias).update_or_create(
        mount="Kowa Six", type='Breech lock', purpose='Camera', manufacturer=Kowa)

    Leitz = Manufacturer.objects.get(name='Leitz')
    Mount.objects.using(db_alias).update_or_create(
        mount="Leica M", shutter_in_lens=0, type='Bayonet', purpose='Camera', manufacturer=Leitz)
    Mount.objects.using(db_alias).update_or_create(
        mount="Leica R", shutter_in_lens=0, type='Bayonet', purpose='Camera', manufacturer=Leitz)

    Mamiya = Manufacturer.objects.get(name='Mamiya')
    Mount.objects.using(db_alias).update_or_create(
        mount="Mamiya 6", type='Bayonet', purpose='Camera', manufacturer=Mamiya)
    Mount.objects.using(db_alias).update_or_create(
        mount="Mamiya 645", type='Bayonet', purpose='Camera', manufacturer=Mamiya)
    Mount.objects.using(db_alias).update_or_create(
        mount="Mamiya 7/7II", type='Bayonet', purpose='Camera', manufacturer=Mamiya)
    Mount.objects.using(db_alias).update_or_create(
        mount="Mamiya RB67", shutter_in_lens=1, type='Bayonet', purpose='Camera', manufacturer=Mamiya)
    Mount.objects.using(db_alias).update_or_create(
        mount="Mamiya RZ67", shutter_in_lens=1, type='Bayonet', purpose='Camera', manufacturer=Mamiya)
    Mount.objects.using(db_alias).update_or_create(
        mount="Mamiya ZE", shutter_in_lens=0, type='Bayonet', purpose='Camera', manufacturer=Mamiya)
    Mount.objects.using(db_alias).update_or_create(mount="Mamiya/Sekor E",
                                                   shutter_in_lens=0, type='Bayonet', purpose='Camera', manufacturer=Mamiya)

    Minolta = Manufacturer.objects.get(name='Minolta')
    Mount.objects.using(db_alias).update_or_create(
        mount="Minolta A", type='Bayonet', purpose='Camera', manufacturer=Minolta)
    Mount.objects.using(db_alias).update_or_create(
        mount="Minolta SR", type='Bayonet', purpose='Camera', manufacturer=Minolta)
    Mount.objects.using(db_alias).update_or_create(
        mount="Miranda M44", type='Bayonet', purpose='Camera', manufacturer=Minolta)

    Nikon = Manufacturer.objects.get(name='Nikon')
    Mount.objects.using(db_alias).update_or_create(
        mount="Nikon F", shutter_in_lens=0, type='Bayonet', purpose='Camera', manufacturer=Nikon)
    Mount.objects.using(db_alias).update_or_create(
        mount="Nikon S", shutter_in_lens=0, type='Bayonet', purpose='Camera', manufacturer=Nikon)

    Olympus = Manufacturer.objects.get(name='Olympus')
    Mount.objects.using(db_alias).update_or_create(
        mount="Olympus OM", shutter_in_lens=0, type='Bayonet', purpose='Camera', manufacturer=Olympus)
    Mount.objects.using(db_alias).update_or_create(
        mount="Olympus Pen F", type='Bayonet', purpose='Camera', manufacturer=Olympus)

    Pentacon = Manufacturer.objects.get(name='Pentacon')
    Mount.objects.using(db_alias).update_or_create(
        mount="Pentacon Six", type='Breech lock', purpose='Camera', manufacturer=Pentacon)
    Mount.objects.using(db_alias).update_or_create(
        mount="Praktica", type='Bayonet', purpose='Camera', manufacturer=Pentacon)
    Mount.objects.using(db_alias).update_or_create(
        mount="Praktina", type='Breech lock', purpose='Camera', manufacturer=Pentacon)

    Pentax = Manufacturer.objects.get(name='Pentax')
    Mount.objects.using(db_alias).update_or_create(
        mount="Pentax 110", type='Bayonet', purpose='Camera', manufacturer=Pentax)
    Mount.objects.using(db_alias).update_or_create(
        mount="Pentax 645", type='Bayonet', purpose='Camera', manufacturer=Pentax)
    Mount.objects.using(db_alias).update_or_create(
        mount="Pentax 6x7", type='Bayonet', purpose='Camera', manufacturer=Pentax)
    Mount.objects.using(db_alias).update_or_create(
        mount="Pentax K", type='Bayonet', purpose='Camera', manufacturer=Pentax)

    Petri = Manufacturer.objects.get(name='Petri')
    Mount.objects.using(db_alias).update_or_create(
        mount="Petriflex", type='Breech lock', purpose='Camera', manufacturer=Petri)

    Rollei = Manufacturer.objects.get(name='Rollei')
    Mount.objects.using(db_alias).update_or_create(
        mount="Rolleiflex SL35", type='Bayonet', purpose='Camera', manufacturer=Rollei)
    Mount.objects.using(db_alias).update_or_create(
        mount="Rolleiflex SL66", type='Bayonet', purpose='Camera', manufacturer=Rollei)

    Sigma = Manufacturer.objects.get(name='Sigma')
    Mount.objects.using(db_alias).update_or_create(
        mount="Sigma SA", shutter_in_lens=0, type='Bayonet', purpose='Camera', manufacturer=Sigma)

    Tamron = Manufacturer.objects.get(name='Tamron')
    Mount.objects.using(db_alias).update_or_create(
        mount="Adaptall", shutter_in_lens=0, type='Bayonet', purpose='Camera', manufacturer=Tamron)

    Zeiss = Manufacturer.objects.get(name='Zeiss Ikon')
    Mount.objects.using(db_alias).update_or_create(
        mount="Contax G", type='Breech lock', purpose='Camera', manufacturer=Zeiss)
    Mount.objects.using(db_alias).update_or_create(
        mount="Contax N", type='Bayonet', purpose='Camera', manufacturer=Zeiss)
    Mount.objects.using(db_alias).update_or_create(
        mount="Contax RF", type='Bayonet', purpose='Camera', manufacturer=Zeiss)
    Mount.objects.using(db_alias).update_or_create(
        mount="Contax/Yashica", type='Bayonet', purpose='Camera', manufacturer=Zeiss)

    Mount.objects.using(db_alias).update_or_create(
        mount="C", shutter_in_lens=0, type='Screw', purpose='Camera')
    Mount.objects.using(db_alias).update_or_create(
        mount="M25 Biological", type='Screw', purpose='Camera')
    Mount.objects.using(db_alias).update_or_create(
        mount="M37", type='Screw', purpose='Camera')
    Mount.objects.using(db_alias).update_or_create(
        mount="M39 (Enlarger)", type='Screw', purpose='Enlarger')
    Mount.objects.using(db_alias).update_or_create(
        mount="M39 (Rangefinder)", shutter_in_lens=0, type='Screw', purpose='Camera')
    Mount.objects.using(db_alias).update_or_create(
        mount="M39 (SLR)", shutter_in_lens=0, type='Screw', purpose='Camera')
    Mount.objects.using(db_alias).update_or_create(
        mount="M42", shutter_in_lens=0, type='Screw', purpose='Camera')
    Mount.objects.using(db_alias).update_or_create(
        mount="Praktiflex", type='Screw', purpose='Camera')
    Mount.objects.using(db_alias).update_or_create(
        mount="T/T2", shutter_in_lens=0, type='Screw', purpose='Camera')


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0006_negative_sizes'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
