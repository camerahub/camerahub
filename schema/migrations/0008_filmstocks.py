from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    db_alias = schema_editor.connection.alias

    Filmstock = apps.get_model("schema", "Filmstock")
    Manufacturer = apps.get_model("schema", "Manufacturer")
    Process = apps.get_model("schema", "Process")

    # Load processes
    BW = Process.objects.get(name='Black & white negative')
    C41 = Process.objects.get(name='C-41')
    E6 = Process.objects.get(name='E-6')
    Polaroid = Process.objects.get(name='Polaroid')
    K14 = Process.objects.get(name='K-14')

    Agfa = Manufacturer.objects.get(name='Agfa')
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Agfa, name="Vista Plus 200", iso=200, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Agfa, name="HDC Plus", iso=200, colour=True, process=C41, panchromatic=True)

    Boots = Manufacturer.objects.get(name='Boots')
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Boots, name="200", iso=200, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Boots, name="200 Colour Slide", iso=200, colour=True, process=E6, panchromatic=True)

    Efke = Manufacturer.objects.get(name='Efke')
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Efke, name="R50", iso=50, colour=False, process=BW, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Efke, name="R25", iso=25, colour=False, process=BW, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Efke, name="IR820", iso=100, colour=False, process=BW, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Efke, name="IR820 Aura", iso=100, colour=False, process=BW, panchromatic=True)

    Fuji = Manufacturer.objects.get(name='Fuji')
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Fuji, name="Reala 100", iso=100, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Fuji, name="Acros 100", iso=100, colour=False, process=BW, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Fuji, name="Neopan 1600", iso=1600, colour=False, process=BW, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Fuji, name="S 400", iso=400, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Fuji, name="S 200", iso=200, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Fuji, name="Pro 160S", iso=160, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Fuji, name="Neopan 400", iso=400, colour=False, process=BW, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Fuji, name="Sensia 200", iso=200, colour=True, process=E6, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Fuji, name="Superia 200", iso=200, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Fuji, name="Velvia 50", iso=50, colour=True, process=E6, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Fuji, name="Velvia 100F", iso=100, colour=True, process=E6, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Fuji, name="Superia X-Tra", iso=400, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Fuji, name="Superia 100", iso=100, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Fuji, name="Unknown Slide", colour=True, panchromatic=True)

    Ilford = Manufacturer.objects.get(name='Ilford')
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Ilford, name="FP4+ 125", iso=125, colour=False, process=BW, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Ilford, name="HP5+ 400", iso=400, colour=False, process=BW, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Ilford, name="Delta 100", iso=100, colour=False, process=BW, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Ilford, name="Delta 400", iso=400, colour=False, process=BW, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Ilford, name="FP3", colour=False, process=BW, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Ilford, name="Pan F+ 50", iso=50, colour=False, process=BW, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Ilford, name="Pan 100", iso=100, colour=False, process=BW, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Ilford, name="Delta 3200", iso=3200, colour=False, process=BW, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Ilford, name="FP4", iso=125, colour=False, process=BW, panchromatic=True)

    Jessops = Manufacturer.objects.get(name='Jessops')
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Jessops, name="Pan 100S", iso=100, colour=False, process=BW, panchromatic=True)

    KawausoShoten = Manufacturer.objects.get(name='Kawauso-Shoten')
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=KawausoShoten, name="Rera Pan", iso=100, colour=False, process=BW, panchromatic=True)

    Kentmere = Manufacturer.objects.get(name='Kentmere')
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kentmere, name="100", iso=100, colour=False, process=BW, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kentmere, name="Select RC", iso=6, colour=False, process=BW, panchromatic=False)

    Kodak = Manufacturer.objects.get(name='Kodak')
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kodak, name="Gold", iso=400, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kodak, name="GT 800", iso=800, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kodak, name="200", iso=200, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kodak, name="VR Plus 400", iso=400, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kodak, name="Ektar 100", iso=100, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kodak, name="Kodacolor 200", iso=200, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kodak, name="Elitechrome 100", iso=100, colour=True, process=E6, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kodak, name="Ektar 125", iso=125, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kodak, name="Gold 200", iso=200, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kodak, name="Kodachrome 40", iso=40, colour=True, process=K14, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kodak, name="Kodalith", iso=12, colour=False, process=BW, panchromatic=False)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kodak, name="Ektachrome 50 Tungsten", iso=50, colour=True, process=E6, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kodak, name="Plus-X pan", iso=125, colour=False, process=BW, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kodak, name="Electron Image Film SO-163", iso=12, colour=False, process=BW, panchromatic=False)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kodak, name="High-Speed Infrared HIE", colour=False, process=BW, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kodak, name="VR Plus 200", iso=200, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Kodak, name="Kodachrome 10", iso=10, colour=True, process=K14, panchromatic=True)

    Konica = Manufacturer.objects.get(name='Konica')
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Konica, name="VX 200", iso=200, colour=True, process=C41, panchromatic=True)

    Maco = Manufacturer.objects.get(name='Maco')
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Maco, name="IR820", iso=400, colour=False, process=BW, panchromatic=True)

    ORWO = Manufacturer.objects.get(name='ORWO')
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=ORWO, name="ORWOChrom UK17", iso=40, colour=True, process=E6, panchromatic=True)

    TheImpossibleProject = Manufacturer.objects.get(
        name='The Impossible Project')
    Filmstock.objects.using(db_alias).update_or_create(manufacturer=TheImpossibleProject,
                                                       name="PX 600 Silver Shade", iso=600, colour=False, process=Polaroid, panchromatic=True)

    Tudor = Manufacturer.objects.get(name='Tudor')
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Tudor, name="Colour 200", iso=200, colour=True, process=C41, panchromatic=True)
    Filmstock.objects.using(db_alias).update_or_create(
        manufacturer=Tudor, name="XLX 100", iso=100, colour=True, process=C41, panchromatic=True)


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0007_mounts'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
