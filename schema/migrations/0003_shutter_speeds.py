from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    db_alias = schema_editor.connection.alias

    ShutterSpeed = apps.get_model("schema", "ShutterSpeed")
    ShutterSpeed.objects.using(db_alias).bulk_create([
        ShutterSpeed(shutter_speed="1/8000", duration="0.000125"),
        ShutterSpeed(shutter_speed="1/6400", duration="0.00015625"),
        ShutterSpeed(shutter_speed="1/6000", duration="0.000166666666667"),
        ShutterSpeed(shutter_speed="1/5000", duration="0.0002"),
        ShutterSpeed(shutter_speed="1/4000", duration="0.00025"),
        ShutterSpeed(shutter_speed="1/3200", duration="0.0003125"),
        ShutterSpeed(shutter_speed="1/3000", duration="0.000333333333333"),
        ShutterSpeed(shutter_speed="1/2500", duration="0.0004"),
        ShutterSpeed(shutter_speed="1/2000", duration="0.0005"),
        ShutterSpeed(shutter_speed="1/1600", duration="0.000625"),
        ShutterSpeed(shutter_speed="1/1500", duration="0.000666666666667"),
        ShutterSpeed(shutter_speed="1/1250", duration="0.0008"),
        ShutterSpeed(shutter_speed="1/1000", duration="0.001"),
        ShutterSpeed(shutter_speed="1/800", duration="0.00125"),
        ShutterSpeed(shutter_speed="1/750", duration="0.001333333333333"),
        ShutterSpeed(shutter_speed="1/640", duration="0.0015625"),
        ShutterSpeed(shutter_speed="1/500", duration="0.002"),
        ShutterSpeed(shutter_speed="1/400", duration="0.0025"),
        ShutterSpeed(shutter_speed="1/350", duration="0.002857142857143"),
        ShutterSpeed(shutter_speed="1/320", duration="0.003125"),
        ShutterSpeed(shutter_speed="1/250", duration="0.004"),
        ShutterSpeed(shutter_speed="1/200", duration="0.005"),
        ShutterSpeed(shutter_speed="1/180", duration="0.005555555555556"),
        ShutterSpeed(shutter_speed="1/160", duration="0.00625"),
        ShutterSpeed(shutter_speed="1/125", duration="0.008"),
        ShutterSpeed(shutter_speed="1/100", duration="0.01"),
        ShutterSpeed(shutter_speed="1/90", duration="0.011111111111111"),
        ShutterSpeed(shutter_speed="1/80", duration="0.0125"),
        ShutterSpeed(shutter_speed="1/60", duration="0.016666666666667"),
        ShutterSpeed(shutter_speed="1/50", duration="0.02"),
        ShutterSpeed(shutter_speed="1/45", duration="0.022222222222222"),
        ShutterSpeed(shutter_speed="1/40", duration="0.025"),
        ShutterSpeed(shutter_speed="1/30", duration="0.033333333333333"),
        ShutterSpeed(shutter_speed="1/25", duration="0.04"),
        ShutterSpeed(shutter_speed="1/20", duration="0.05"),
        ShutterSpeed(shutter_speed="1/15", duration="0.066666666666667"),
        ShutterSpeed(shutter_speed="1/13", duration="0.076923076923077"),
        ShutterSpeed(shutter_speed="1/10", duration="0.1"),
        ShutterSpeed(shutter_speed="1/8", duration="0.125"),
        ShutterSpeed(shutter_speed="1/6", duration="0.166666666666667"),
        ShutterSpeed(shutter_speed="1/5", duration="0.2"),
        ShutterSpeed(shutter_speed="1/4", duration="0.25"),
        ShutterSpeed(shutter_speed="1/3", duration="0.333333333333333"),
        ShutterSpeed(shutter_speed="1/2.5", duration="0.4"),
        ShutterSpeed(shutter_speed="1/2", duration="0.5"),
        ShutterSpeed(shutter_speed="1/1.5", duration="0.666666666666667"),
        ShutterSpeed(shutter_speed="1", duration="1"),
        ShutterSpeed(shutter_speed="1.3", duration="1.3"),
        ShutterSpeed(shutter_speed="1.5", duration="1.5"),
        ShutterSpeed(shutter_speed="1.6", duration="1.6"),
        ShutterSpeed(shutter_speed="1/0.6", duration="1.66666666666667"),
        ShutterSpeed(shutter_speed="2", duration="2"),
        ShutterSpeed(shutter_speed="2.5", duration="2.5"),
        ShutterSpeed(shutter_speed="3", duration="3"),
        ShutterSpeed(shutter_speed="1/0.3", duration="3.33333333333333"),
        ShutterSpeed(shutter_speed="4", duration="4"),
        ShutterSpeed(shutter_speed="5", duration="5"),
        ShutterSpeed(shutter_speed="6", duration="6"),
        ShutterSpeed(shutter_speed="8", duration="8"),
        ShutterSpeed(shutter_speed="10", duration="10"),
        ShutterSpeed(shutter_speed="12", duration="12"),
        ShutterSpeed(shutter_speed="13", duration="13"),
        ShutterSpeed(shutter_speed="16", duration="16"),
        ShutterSpeed(shutter_speed="20", duration="20"),
        ShutterSpeed(shutter_speed="24", duration="24"),
        ShutterSpeed(shutter_speed="26", duration="26"),
        ShutterSpeed(shutter_speed="30", duration="30")
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0002_data'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
