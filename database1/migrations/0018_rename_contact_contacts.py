# Generated by Django 4.2.7 on 2023-12-01 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database1', '0017_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='contacts',
        ),
    ]
