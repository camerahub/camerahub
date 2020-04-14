from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    db_alias = schema_editor.connection.alias

    NegativeSize = apps.get_model("schema", "NegativeSize")
    NegativeSize.objects.using(db_alias).bulk_create([
        NegativeSize(name="6x7", width="70", height="56",
                     crop_factor="0.48", area="3920", aspect_ratio="1.25"),
        NegativeSize(name="6x6", width="56", height="56",
                     crop_factor="0.55", area="3136", aspect_ratio="1"),
        NegativeSize(name="6x4.5", width="56", height="41.5",
                     crop_factor="0.62", area="2324", aspect_ratio="1.35"),
        NegativeSize(name="6x9", width="84", height="56",
                     crop_factor="0.43", area="4704", aspect_ratio="1.5"),
        NegativeSize(name="35mm", width="36", height="24",
                     crop_factor="1", area="864", aspect_ratio="1.5"),
        NegativeSize(name="APS-C", width="22.2", height="14.8",
                     crop_factor="1.62", area="329", aspect_ratio="1.5"),
        NegativeSize(name="35mm half frame", width="18", height="24",
                     crop_factor="1.44", area="432", aspect_ratio="0.75"),
        NegativeSize(name="1/1.6\"", width="8", height="6",
                     crop_factor="4.33", area="48", aspect_ratio="1.33"),
        NegativeSize(name="Quarter plate", width="110", height="82.6",
                     crop_factor="0.31", area="9086", aspect_ratio="1.33"),
        NegativeSize(name="Integral 600", width="79", height="79",
                     crop_factor="0.39", area="6241", aspect_ratio="1"),
        NegativeSize(name="35mm panoramic", width="36", height="12",
                     crop_factor="1.14", area="432", aspect_ratio="3"),
        NegativeSize(name="6.5x9", width="88.9", height="63.5",
                     crop_factor="0.4", area="5645", aspect_ratio="1.4"),
        NegativeSize(name="2.25x3.25\"", width="82", height="57",
                     crop_factor="0.43", area="4674", aspect_ratio="1.44"),
        NegativeSize(name="4x5", width="125", height="100",
                     crop_factor="0.27", area="12500", aspect_ratio="1.25"),
        NegativeSize(name="8x10", width="238", height="190",
                     crop_factor="0.14", area="45220", aspect_ratio="1.25"),
        NegativeSize(name="126", width="28", height="28",
                     crop_factor="1.09", area="784", aspect_ratio="1"),
        NegativeSize(name="110", width="17", height="13",
                     crop_factor="2.02", area="221", aspect_ratio="1.31"),
        NegativeSize(name="1\"x1\"", width="24", height="24",
                     crop_factor="1.27", area="576", aspect_ratio="1"),
        NegativeSize(name="2.5\" x 4.25\"", width="108", height="63.5",
                     crop_factor="0.35", area="6658", aspect_ratio="1.7"),
        NegativeSize(name="6x11", width="108", height="55",
                     crop_factor="0.36", area="5940", aspect_ratio="1.96"),
        NegativeSize(name="1?x2½\"", width="60", height="40",
                     crop_factor="0.6", area="2400", aspect_ratio="1.5"),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0005_formats'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
