# Generated by Django 3.1.4 on 2020-12-24 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrancemeasure',
            old_name='Data',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='entrancemeasure',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='entrancemeasure',
            old_name='EntranceID',
            new_name='id',
        ),
    ]
