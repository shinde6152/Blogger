# Generated by Django 4.2.7 on 2023-11-26 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database1', '0014_alter_blog_heading_alter_blog_heading2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='image',
            new_name='image11',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='image2',
            new_name='image22',
        ),
    ]
