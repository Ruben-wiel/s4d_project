# Generated by Django 3.0.6 on 2020-06-02 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_remove_post_favourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='categorie',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titel',
        ),
    ]
