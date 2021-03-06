# Generated by Django 2.2.17 on 2021-02-16 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0118_auto_20210203_2108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cameramodel',
            old_name='image_attribution_url',
            new_name='image_attribution_link',
        ),
        migrations.RenameField(
            model_name='cameramodel',
            old_name='linkurl',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='enlargermodel',
            old_name='image_attribution_url',
            new_name='image_attribution_link',
        ),
        migrations.RenameField(
            model_name='flashmodel',
            old_name='image_attribution_url',
            new_name='image_attribution_link',
        ),
        migrations.RenameField(
            model_name='historicalcameramodel',
            old_name='image_attribution_url',
            new_name='image_attribution_link',
        ),
        migrations.RenameField(
            model_name='historicalcameramodel',
            old_name='linkurl',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='historicalenlargermodel',
            old_name='image_attribution_url',
            new_name='image_attribution_link',
        ),
        migrations.RenameField(
            model_name='historicalflashmodel',
            old_name='image_attribution_url',
            new_name='image_attribution_link',
        ),
        migrations.RenameField(
            model_name='historicallensmodel',
            old_name='diagram_attribution_url',
            new_name='diagram_attribution_link',
        ),
        migrations.RenameField(
            model_name='historicallensmodel',
            old_name='image_attribution_url',
            new_name='image_attribution_link',
        ),
        migrations.RenameField(
            model_name='historicallensmodel',
            old_name='linkurl',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='historicalmanufacturer',
            old_name='linkurl',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='historicalteleconvertermodel',
            old_name='image_attribution_url',
            new_name='image_attribution_link',
        ),
        migrations.RenameField(
            model_name='lensmodel',
            old_name='diagram_attribution_url',
            new_name='diagram_attribution_link',
        ),
        migrations.RenameField(
            model_name='lensmodel',
            old_name='image_attribution_url',
            new_name='image_attribution_link',
        ),
        migrations.RenameField(
            model_name='lensmodel',
            old_name='linkurl',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='manufacturer',
            old_name='linkurl',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='teleconvertermodel',
            old_name='image_attribution_url',
            new_name='image_attribution_link',
        ),
    ]
