# Generated by Django 2.2.4 on 2019-11-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0015_auto_20191107_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lensmodel',
            name='url',
            field=models.URLField(blank=True, help_text='URL to more information about this lens', null=True, verbose_name='URL'),
        ),
    ]