# Generated by Django 3.0.6 on 2020-05-28 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20200528_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(choices=[('Klusjes', 'Klusjes'), ('Uitlaatservice', 'Uitlaatservice'), ('Boodschappen', 'Boodschappen')], to='website.Category'),
        ),
    ]
