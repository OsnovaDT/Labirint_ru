# Generated by Django 3.1.2 on 2020-11-08 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_author_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='genre',
            new_name='genres',
        ),
    ]
