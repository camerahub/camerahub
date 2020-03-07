# Generated by Django 2.2.9 on 2020-03-05 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0023_auto_20200304_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='cameramodel',
            name='shoe',
            field=models.CharField(blank=True, choices=[('No shoe', 'No shoe'), ('Hot shoe', 'Hot shoe'), ('Cold shoe', 'Cold shoe')], help_text='Type of flash/accessory shoe used on this camera model', max_length=9, null=True),
        ),
    ]