# Generated by Django 4.2.7 on 2023-11-22 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database1', '0011_belize'),
    ]

    operations = [
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
