# Generated by Django 3.0.6 on 2020-06-02 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='adres',
            new_name='adress',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='telefoonnummer',
            new_name='phone',
        ),
    ]
