# Generated by Django 3.1.2 on 2020-11-08 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20201108_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='info',
        ),
    ]
