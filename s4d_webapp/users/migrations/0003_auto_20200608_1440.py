# Generated by Django 3.0.6 on 2020-06-08 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200602_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='adress',
            new_name='adres',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='phone',
            new_name='telefoon',
        ),
    ]
