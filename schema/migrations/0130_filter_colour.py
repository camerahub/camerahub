# Generated by Django 3.2.12 on 2022-03-31 15:33

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0129_auto_20211109_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='colour',
            field=colorfield.fields.ColorField(blank=True, default=None, help_text='Colour of the filter', image_field=None, max_length=18, null=True, samples=None),
        ),
    ]
