from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0125_auto_20210517_2102'),
        ('sphinxdoc', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql=[("INSERT INTO sphinxdoc_project (id, name, slug, path) VALUES (1, 'CameraHub', 'camerahub', 'docs');")],
            reverse_sql=[("DELETE FROM sphinxdoc_project where id=1;")],
        )
    ]
