# Generated by Django 3.0.6 on 2020-05-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20200528_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(choices=[('Klusjes', 'Klusjes'), ('Uitlaatservice', 'Uitlaatservice'), ('Boodschappen', 'Boodschappen')], max_length=100, to='website.Category'),
        ),
    ]
