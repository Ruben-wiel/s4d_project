# Generated by Django 3.0.6 on 2020-06-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0027_auto_20200604_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='beschrijving',
            field=models.TextField(max_length=500),
        ),
    ]
