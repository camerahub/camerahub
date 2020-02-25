# Generated by Django 2.2 on 2020-02-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0020_create_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='cameramodel',
            name='disambiguation',
            field=models.CharField(blank=True, help_text='Distinguishing notes for camera models with the same name', max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='lensmodel',
            name='disambiguation',
            field=models.CharField(blank=True, help_text='Distinguishing notes for lens models with the same name', max_length=45, null=True),
        ),
    ]