# Generated by Django 2.2.14 on 2020-09-04 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0082_auto_20200828_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='cameramodel',
            name='external_power_drive',
            field=models.BooleanField(blank=True, help_text='Whether the camera supports an external power drive', null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='interchangeable_backs',
            field=models.BooleanField(blank=True, help_text='Whether the camera has interchangeable backs', null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='interchangeable_finders',
            field=models.BooleanField(blank=True, help_text='Whether the camera has interchangeable finders', null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='multiple_exposures',
            field=models.BooleanField(blank=True, help_text='Whether the camera can do multiple exposures', null=True),
        ),
        migrations.AddField(
            model_name='cameramodel',
            name='strap_lugs',
            field=models.BooleanField(blank=True, help_text='Whether the camera has strap lugs', null=True),
        ),
        migrations.AddField(
            model_name='historicalcameramodel',
            name='external_power_drive',
            field=models.BooleanField(blank=True, help_text='Whether the camera supports an external power drive', null=True),
        ),
        migrations.AddField(
            model_name='historicalcameramodel',
            name='interchangeable_backs',
            field=models.BooleanField(blank=True, help_text='Whether the camera has interchangeable backs', null=True),
        ),
        migrations.AddField(
            model_name='historicalcameramodel',
            name='interchangeable_finders',
            field=models.BooleanField(blank=True, help_text='Whether the camera has interchangeable finders', null=True),
        ),
        migrations.AddField(
            model_name='historicalcameramodel',
            name='multiple_exposures',
            field=models.BooleanField(blank=True, help_text='Whether the camera can do multiple exposures', null=True),
        ),
        migrations.AddField(
            model_name='historicalcameramodel',
            name='strap_lugs',
            field=models.BooleanField(blank=True, help_text='Whether the camera has strap lugs', null=True),
        ),
    ]
