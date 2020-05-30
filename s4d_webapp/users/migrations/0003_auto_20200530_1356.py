# Generated by Django 3.0.5 on 2020-05-30 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200530_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='locatie',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='adres',
            field=models.CharField(default=True, help_text='Straat + huisnummer', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='telefoonnummer',
            field=models.CharField(help_text='Vul 06-, +316- of Huis- nummer in', max_length=12),
        ),
    ]
