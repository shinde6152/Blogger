# Generated by Django 4.2.7 on 2023-12-01 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database1', '0016_rename_field_type_fieldtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('message', models.TextField()),
            ],
        ),
    ]
