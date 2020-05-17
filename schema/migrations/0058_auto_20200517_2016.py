# Generated by Django 2.2.12 on 2020-05-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0057_remove_camera_display_lens'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='shortname',
            field=models.CharField(blank=True, help_text='Filter type shortname (e.g. Red, CPL, UV)', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='type',
            field=models.CharField(help_text='Filter type (e.g. Red, Circular polariser, Ultraviolet)', max_length=45),
        ),
    ]
