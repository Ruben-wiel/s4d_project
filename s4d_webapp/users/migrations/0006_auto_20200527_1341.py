# Generated by Django 3.0.6 on 2020-05-27 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200527_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='biography',
            field=models.CharField(default=False, max_length=250),
        ),
    ]