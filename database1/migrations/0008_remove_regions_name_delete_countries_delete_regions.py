# Generated by Django 4.2.7 on 2023-11-16 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database1', '0007_rename_countries_countries_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regions',
            name='name',
        ),
        migrations.DeleteModel(
            name='countries',
        ),
        migrations.DeleteModel(
            name='regions',
        ),
    ]
